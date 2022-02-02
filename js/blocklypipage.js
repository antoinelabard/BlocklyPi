/**
 * Create the core JS object needed for every BlocklyPi page.
 */
var BlocklyPiPage = function (blocklyWorkspace) {

    this._blocklyWorkspace = blocklyWorkspace;
    this._highlightPause = false;
    this._blockEventListeners = {};
    this._blockEventListenerTypes = {};
    this._lastExecutedMode = "RUN";

};

/**
 * Run the Blockly Script, currently in the worksapce, without delay and highlighting
 * of the blocks.
 */
BlocklyPiPage.prototype.executeBlocklyWorkspace = function () {

    // Remove all previously registered listeners from our custom Blockly  from an older run.
    this.removeAllEventListeners();

    var code = Blockly.JavaScript.workspaceToCode(this._blocklyWorkspace);
    var interpreter = new Interpreter(code, this.initApi.bind(this));
    this.runBlocklyScript(interpreter);
}

/**
 * Run the Blockly Script, currently in the worksapce, delay every step a bit and highlight
 * the currently executing Blockly block.
 */
BlocklyPiPage.prototype.debugBlocklyWorkspace = function () {

    // Remove all previously registered listeners from an older run.
    this.removeAllEventListeners();

    window.LoopTrap = 10000;
    Blockly.JavaScript.STATEMENT_PREFIX = 'highlightBlock(%1);\n';
    Blockly.JavaScript.addReservedWords('highlightBlock');
    var code = Blockly.JavaScript.workspaceToCode(this._blocklyWorkspace);

    // Debug it ...
    var interpreter = new Interpreter(code, this.initApi.bind(this));
    this.debugBlocklyScript(interpreter);
}

/**
 * Stop executing the current script. (Script can only be interrupted in debug mode).
 */
BlocklyPiPage.prototype.stopBlocklyWorkspace = function () {

    // Set the global executing variable on false, this will signal the stopping
    // of the current script (if it's currently executing).
    this._executingScript = false;

    // Reset the robot.
    // Just stopping it is enough for now ...
    this.runPiRobotCommand("FrancasterController.setMotorPower", "RIGHT", 0);
    this.runPiRobotCommand("FrancasterController.setMotorPower", "LEFT", 0);

    // Remove all previously registered listeners from an older run.
    this.removeAllEventListeners();

}


/**
 * Start running the blugly script in the passed interpreter.
 *
 * @param interpreter The JS-interpreter holding the Blockly script to be
 *            executed.
 */
BlocklyPiPage.prototype.runBlocklyScript = function (interpreter) {

    // Set the last executed mode to "RUN"
    this._lastExecutedMode = "RUN";

    // Start executing.
    interpreter.run();

}

/**
 *
 * @param interpreter The JS-interpreter holding the Blockly script to be
 *            executed.
 */
BlocklyPiPage.prototype.debugBlocklyScript = function (interpreter) {

    var self = this;

    // Function to recursively step through the code ...
    var nextStep = function () {
        if (interpreter.step()) {
            window.setTimeout(nextStep, 10);
        }
    };

    // Settings to make sure that we can highlight the blocks.
    this._blocklyWorkspace.traceOn(true);
    this._blocklyWorkspace.highlightBlock(null);

    // Set the last executed mode to "DEBUG"
    this._lastExecutedMode = "DEBUG";

    // Start recursively stepping ...
    nextStep();
}


/**
 * This method registers all the API calls on the interpreter that executes
 * the JS script generated by the Blockly script in the workspace of the page.
 *
 * All methods that are generated by custom Blockly blocks that are not standard
 * JS (sending robot motor speed, DOM interaction, etc.) schould be registered
 * as "API calls"  here.
 *
 * See "Add an API" at: https://developers.google.com/blockly/installation/js-interpreter
 *
 * @param interpreter The interpreter for which to set the API calls.
 * @param scope The current scope of the interpreter.
 */
BlocklyPiPage.prototype.initApi = function (interpreter, scope) {

    var self = this;

    // Add an API function for the alert() block.
    var alertWrapper = function (text) {
        text = text ? text.toString() : '';
        return interpreter.createPrimitive(alert(text));
    };
    interpreter.setProperty(scope, 'alert', interpreter.createNativeFunction(alertWrapper));

    // Add an API function for the prompt() block.
    var promptWrapper = function (text) {
        text = text ? text.toString() : '';
        return interpreter.createPrimitive(prompt(text));
    };
    interpreter.setProperty(scope, 'prompt', interpreter.createNativeFunction(promptWrapper));

    // Add an API function for highlighting blocks in the workspace.
    var highlightingWrapper = function (id) {
        id = id ? id.toString() : '';
        return interpreter.createPrimitive(self.highlightBlock(id));
    };
    interpreter.setProperty(scope, 'highlightBlock', interpreter.createNativeFunction(highlightingWrapper));

    // Add an API function for adding a key event listener.
    var addKeyEventListenerForBlockWrapper = function (id, type, callbackCode) {
        id = id ? id.toString() : '';
        type = type ? type.toString() : '';
        callbackCode = callbackCode ? callbackCode.toString() : '';
        return interpreter.createPrimitive(self.addKeyEventListenerForBlock(id, type, callbackCode));
    };
    interpreter.setProperty(scope, 'addKeyEventListenerForBlock',
        interpreter.createNativeFunction(addKeyEventListenerForBlockWrapper));

    // Add an API function for setting the power of the robot motors.
    var runPiRobotCommandWrapper = function () {

        // Convert the arguments to normal JS primitives ...
        for (var i = 0; i < arguments.length; i++) {
            if (arguments[i].type === "string") {
                arguments[i] = arguments[i].toString();
            } else if (arguments[i].type === "number") {
                arguments[i] = arguments[i].toNumber();
            } else if (arguments[i].type === "boolean") {
                arguments[i] = arguments[i].toBoolean();
            } else {
                // An Array, Object or Function ... This is not unsupported at the moment, don't know how ...
                // Just converting it as a string I guess ...
                arguments[i] = arguments[i].valueOf();
            }
        }
        // Execute the "runPiRobotCommand" on these arguments.
        return interpreter.createPrimitive(self.runPiRobotCommand.apply(self, arguments));
    };
    interpreter.setProperty(scope, 'runPiRobotCommand', interpreter.createNativeFunction(runPiRobotCommandWrapper));

    // Add an API function for resetting the robot.
    var resetRobotWrapper = function () {
        return interpreter.createPrimitive(self.resetRobot());
    };
    interpreter.setProperty(scope, 'resetRobot', interpreter.createNativeFunction(resetRobotWrapper));

}

/**
 * Highlight the targeted block in the Blockly workspace of this page.
 *
 * This method gets called from the Interpreter API (@see BlocklyPiPage.prototype.initApi).
 *
 * @param id
 */
BlocklyPiPage.prototype.highlightBlock = function (id) {
    this._blocklyWorkspace.highlightBlock(id);
    this._highlightPause = true;
}

/**
 * Run a robot command on the RaspBerry Pi (over XML-RPC).
 *
 * The first argument is the name of the method to call on the Pi.
 * All the other arguments are the parameters of that method.
 *
 * e.g.: runPiRobotCommand("FrancasterController.setMotorPower","LEFT", 80);
 *
 * Keep in mind that this method does not return the result of the XML-RPC method. If this
 * is necessary, use @see BlocklyPiPage.prototype.returnPiRobotCommandResult.
 */
BlocklyPiPage.prototype.runPiRobotCommand = function () {

    var self = this;

    // Convert arguments to an array.
    var args = Array.prototype.slice.call(arguments);

    // Extract the rpc method to call and it's parameters.
    var rpcMethod = args[0];
    var rpcParameters = args.slice(1, args.length);

    // Make the rpc call ...
    $.xmlrpc({
        url: '/RobotControlService',
        methodName: rpcMethod,
        params: rpcParameters,
        success: function (response, status, jqXHR) {
            // Do nothing, interested? Use returnPiRobotCommandResult.
        },
        error: function (jqXHR, status, error) {
            self.displayErrorMsg(error);
        }
    });
}

/**
 * Run a robot command on the RaspBerry Pi (over XML-RPC).
 *
 * The first argument is the name of the method to call on the Pi.
 * All the other arguments are the parameters of that method.
 *
 * e.g.: distance = returnPiRobotCommandResult("getSonarVal");
 *
 * Keep in mind that this method does block until the result of the XML-RPC method is
 * returned. Use @see BlocklyPiPage.prototype.runPiRobotCommand if you're not interested
 * in the result, it's faster.
 */
BlocklyPiPage.prototype.returnPiRobotCommandResult = function () {

    var self = this;

    // Convert arguments to an array.
    var args = Array.prototype.slice.call(arguments);

    // Extract the rpc method to call and it's parameters.
    var rpcMethod = args[0];
    var rpcParameters = args.slice(1, args.length);

    // Variable that keeps track whether the xml-rpc request returned or not.
    var xmlRpcReturned = false;

    // The response to be returned.
    var returnedResponse = undefined;

    // Make the rpc call ...
    $.xmlrpc({
        url: '/RobotControlService',
        methodName: rpcMethod,
        params: rpcParameters,
        success: function (response, status, jqXHR) {
            returnedResponse = response;
        },
        error: function (jqXHR, status, error) {
            self.displayErrorMsg(error);
        }
    });

    // Block until response is set.
    while (!xmlRpcReturned) {
        // do nothing ...	
    }

    // returnedResponse is set now ...
    return returnedResponse;
}


/**
 * Register a key listener for one of our custom blocks that listen to keyup/keydown events.
 *
 * The callbackCode can only make use of the "keyCode" and "charCode" variables (We could not
 * add the whole event object to the interpreter's sandbox.)
 *
 * @param id The id of the block that wants to register the event listener (we only allow one
 *        event listener for every block).
 * @param type The type of key event listener to register (can be either "keyup" or "keydown").
 * @param callbackCode The code to run in an interpreter when the event get's executed (can only
 *        make use of global "keyCode" and "charCode" variables).
 */
BlocklyPiPage.prototype.addKeyEventListenerForBlock = function (id, type, callbackCode) {

    var self = this;

    // Allow only one event listener for a block.
    if (this._blockEventListeners[id]) {
        console.log("Block " + id + " already has one event listener associated with it! Ignoring this one.");
        return;
    }

    // Register this key event listener
    this._blockEventListenerTypes[id] = type;
    this._blockEventListeners[id] = function (event) {

        // Add the event variable as a global variable in the JS interpreter.
        // Therefore we need to add this the API init function.
        var newApitInt = function (interpreter, scope) {
            this.initApi(interpreter, scope);
            interpreter.setProperty(scope, 'keyCode', interpreter.createPrimitive(event.keyCode));
            interpreter.setProperty(scope, 'charCode', interpreter.createPrimitive(event.keyCode));
        }

        // Init a new interpreter for this.
        interpreter = new Interpreter(callbackCode, newApitInt.bind(self));

        // Check whether the last ran execution mode was "DEBUG".
        if (self._lastExecutedMode === "DEBUG") {
            // Last ran execution mode was "DEBUG", run the same.
            self.debugBlocklyScript(interpreter);
        } else {
            // Run in normal mode.
            self.runBlocklyScript(interpreter);
        }

    }

    // Change color of the block to indicate that listener has been set. 
    // Feel free to change to other color.
    this._blocklyWorkspace.getBlockById(id).setColour(0);

    // Add the listener to the window.
    window.addEventListener(type, this._blockEventListeners[id]);
}

/**
 * For all blocks, remove all the event listeners. Get's executed before every rerun.
 */
BlocklyPiPage.prototype.removeAllEventListeners = function () {
    // Iterate over all registered event listeners
    for (var id in this._blockEventListeners) {
        if (this._blockEventListeners.hasOwnProperty(id)) {

            // Remove the listener ...
            window.removeEventListener(this._blockEventListenerTypes[id],
                this._blockEventListeners[id]);

            // Clear their references ...
            this._blockEventListeners[id] = undefined;
            this._blockEventListenerTypes[id] = undefined;

            // Assign the default color again ...
            try {
                this._blocklyWorkspace.getBlockById(id).setColour(210);
            } catch (e) {
                // Block was probably deleted.
            }
        }
    }
}

/**
 * Display an error message on the page.
 *
 * @msg The message to display.
 */
BlocklyPiPage.prototype.displayErrorMsg = function (msg) {
    $("#errorMessage").text(msg);
    $("#errorMsgContainer").show();
}
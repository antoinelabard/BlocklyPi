Blockly.JavaScript['control_key_down'] = function (block) {
    // The inputs ...
    var statements_statements = Blockly.JavaScript.statementToCode(block, 'STATEMENTS');
    var dropdown_key = block.getFieldValue('KEY');

    // Determine the key code to listen for.
    var keyCode = 0;
    if (dropdown_key === 'UP') {
        keyCode = 38;
    } else if (dropdown_key === 'DOWN') {
        keyCode = 40;
    } else if (dropdown_key === 'RIGHT') {
        keyCode = 39;
    } else if (dropdown_key === 'LEFT') {
        keyCode = 37;
    } else if (dropdown_key === 'a') {
        keyCode = 65;
    } else if (dropdown_key === 'b') {
        keyCode = 66;
    } else if (dropdown_key === 'c') {
        keyCode = 67;
    } else if (dropdown_key === 'd') {
        keyCode = 68;
    } else if (dropdown_key === 'e') {
        keyCode = 69;
    } else if (dropdown_key === 'f') {
        keyCode = 70;
    } else if (dropdown_key === 'g') {
        keyCode = 71;
    } else if (dropdown_key === 'h') {
        keyCode = 72;
    } else if (dropdown_key === 'i') {
        keyCode = 73;
    } else if (dropdown_key === 'j') {
        keyCode = 74;
    } else if (dropdown_key === 'k') {
        keyCode = 75;
    } else if (dropdown_key === 'l') {
        keyCode = 76;
    } else if (dropdown_key === 'm') {
        keyCode = 77;
    } else if (dropdown_key === 'n') {
        keyCode = 78;
    } else if (dropdown_key === 'o') {
        keyCode = 79;
    } else if (dropdown_key === 'p') {
        keyCode = 80;
    } else if (dropdown_key === 'q') {
        keyCode = 81;
    } else if (dropdown_key === 'r') {
        keyCode = 82;
    } else if (dropdown_key === 's') {
        keyCode = 83;
    } else if (dropdown_key === 't') {
        keyCode = 84;
    } else if (dropdown_key === 'u') {
        keyCode = 85;
    } else if (dropdown_key === 'v') {
        keyCode = 86;
    } else if (dropdown_key === 'w') {
        keyCode = 87;
    } else if (dropdown_key === 'x') {
        keyCode = 88;
    } else if (dropdown_key === 'y') {
        keyCode = 89;
    } else if (dropdown_key === 'z') {
        keyCode = 90;
    } else if (dropdown_key === '0') {
        keyCode = 96;
    } else if (dropdown_key === '1') {
        keyCode = 97;
    } else if (dropdown_key === '2') {
        keyCode = 98;
    } else if (dropdown_key === '3') {
        keyCode = 99;
    } else if (dropdown_key === '4') {
        keyCode = 100;
    } else if (dropdown_key === '5') {
        keyCode = 101;
    } else if (dropdown_key === '6') {
        keyCode = 102;
    } else if (dropdown_key === '7') {
        keyCode = 103;
    } else if (dropdown_key === '8') {
        keyCode = 104;
    } else if (dropdown_key === '9') {
        keyCode = 105;
    } else {
        return '';
    }

    // Determine the type of event to listen to.
    var type = "keyup";
    // Generate the code for the callback (using only keyCode an charCode).
    var callbackCode = 'var code = keyCode; if (charCode && code == 0) {code = charCode;}; if (code ===' + keyCode + ') {' + statements_statements + '}';
    callbackCode = callbackCode.replace(/\n/g, "\\n");
    callbackCode = callbackCode.replace(/["]+/g, "\\\"");

    // Assemble JavaScript into code variable.
    var code = 'window.addKeyEventListenerForBlock("' + block.id + '", "' + type + '", "' + callbackCode + '");';
    return code;
};

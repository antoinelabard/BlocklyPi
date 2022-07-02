const ALLBOTS_COLOR = 0;

function getMotorDropdown() {
    return new Blockly.FieldDropdown([
        ["0", "0"],
        ["1", "1"],
        ["2", "2"],
        ["3", "3"],
        ["4", "4"],
        ["5", "5"],
        ["6", "6"],
        ["7", "7"],
    ]);
}

Blockly.Blocks['allbots-set_motor_position'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Mettre le moteur")
            .appendField(getMotorDropdown(), "MOTOR_NB");
        this.appendDummyInput()
            .setAlign(Blockly.ALIGN_RIGHT)
            .appendField("à")
            .appendField(new Blockly.FieldTextInput("0"), "ANGLE")
            .appendField("degrés.");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(ALLBOTS_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['allbots-shift_motor_position'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Faire")
            .appendField(new Blockly.FieldDropdown([
                ["avancer", "FORWARD"],
                ["reculer", "BACKWARD"]
            ]), "DIRECTION")
            .appendField("le moteur")
            .appendField(getMotorDropdown(), "MOTOR_NB");
        this.appendDummyInput()
            .setAlign(Blockly.ALIGN_RIGHT)
            .appendField("de")
            .appendField(new Blockly.FieldTextInput("0"), "SHIFT_ANGLE")
            .appendField("degrés");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(ALLBOTS_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['allbots-reset_position'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Remettre a la position initiale")
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(ALLBOTS_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['allbots-move_forward'] = {
    init: function() {
        this.appendDummyInput()
            .appendField("Avancer le Robot ");
        this.setInputsInline(false);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(ALLBOTS_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['allbots-move_backward'] = {
    init: function() {
        this.appendDummyInput()
            .appendField("Reculer le Robot ");
        this.setInputsInline(false);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(ALLBOTS_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['allbots-turn_left'] = {
    init: function() {
        this.appendDummyInput()
            .setAlign(Blockly.ALIGN_CENTRE)
            .appendField("Tourner à gauche");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(ALLBOTS_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['allbots-turn_right'] = {
    init: function() {
        this.appendDummyInput()
            .setAlign(Blockly.ALIGN_CENTRE)
            .appendField("Tourner à droite");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(ALLBOTS_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['allbots-do_hi'] = {
    init: function() {
        this.appendDummyInput()
            .appendField("Faire coucou avec la patte ")
            .appendField(new Blockly.FieldDropdown([["gauche","0"], ["droite","1"]]), "motor");

        this.setInputsInline(true);
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(ALLBOTS_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};
Blockly.Blocks['allbots-sleep'] = {
    init: function () {
        this.appendValueInput("NBR_SEC").appendField("Dormir pendant");
        this.appendDummyInput().appendField("secondes");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(ALLBOTS_COLOR);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};
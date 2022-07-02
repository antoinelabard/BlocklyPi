Blockly.JavaScript['allbots-set_motor_position'] = function (block) {
    var dropdown_motor_nb = block.getFieldValue('MOTOR_NB');
    var angle = block.getFieldValue('ANGLE');

    return `runPiRobotCommand("allbots-set_motor_position", "${dropdown_motor_nb}","${angle}");`;
};

Blockly.JavaScript['allbots-shift_motor_position'] = function (block) {
    var dropdown_direction = block.getFieldValue('DIRECTION');
    var dropdown_motor_nb = block.getFieldValue('MOTOR_NB');
    var shift_angle = parseInt(block.getFieldValue('SHIFT_ANGLE'));

    if (dropdown_direction === "BACKWARD") {
        shift_angle = -shift_angle
    }

    return `runPiRobotCommand("allbots-shift_motor_position", "${dropdown_motor_nb}", "${shift_angle}");`;
};

Blockly.JavaScript['allbots-reset_position'] = function (block) {
    return `runPiRobotCommand("allbots-reset_position");`;
};

Blockly.JavaScript['allbots-move_forward'] = function(block) {
    return 'runPiRobotCommand("allbots-move_forward");';
};

Blockly.JavaScript['allbots-move_backward'] = function(block) {
    return 'runPiRobotCommand("allbots-move_backward");';
};

Blockly.JavaScript['allbots-turn_left'] = function(block) {
    return 'runPiRobotCommand("allbots-turn_left");';
};

Blockly.JavaScript['allbots-turn_right'] = function(block) {
    return 'runPiRobotCommand("allbots-turn_right");';
};

Blockly.JavaScript['allbots-do_hi'] = function(block) {
    var dropdown_motor = block.getFieldValue('motor');
    return 'runPiRobotCommand("allbots-do_hi", "' + dropdown_motor + '");';
};

Blockly.JavaScript['allbots-sleep'] = function (block) {
    var value_time = Blockly.JavaScript.valueToCode(block, 'NBR_SEC', Blockly.JavaScript.ORDER_ATOMIC);
    return 'runPiRobotCommand("FrancasterController.allbots-sleep", ' + value_time + ');';
};
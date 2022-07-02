Blockly.JavaScript['francaster-set_motor_position'] = function (block) {
    var dropdown_motor_nb = block.getFieldValue('MOTOR_NB');
    var angle = block.getFieldValue('ANGLE');

    return `runPiRobotCommand("francaster-set_motor_position", "${dropdown_motor_nb}","${angle}");`;
};

Blockly.JavaScript['francaster-shift_motor_position'] = function (block) {
    var dropdown_direction = block.getFieldValue('DIRECTION');
    var dropdown_motor_nb = block.getFieldValue('MOTOR_NB');
    var shift_angle = parseInt(block.getFieldValue('SHIFT_ANGLE'));

    if (dropdown_direction === "BACKWARD") {
        shift_angle = -shift_angle
    }

    return `runPiRobotCommand("francaster-shift_motor_position", "${dropdown_motor_nb}", "${shift_angle}");`;
};

Blockly.JavaScript['francaster-speak'] = function (block) {
    var text_qstn = block.getFieldValue('QSTN');
    return `runPiRobotCommand("francaster-speak", "${text_qstn}");`;
};

Blockly.JavaScript['francaster-repeat'] = function (block) {
    return `runPiRobotCommand("repeat");`;
};

Blockly.JavaScript['francaster-answer_question'] = function (block) {
    var text_qstn = block.getFieldValue('QSTN');
    return `runPiRobotCommand("francaster-answer_question", "${text_qstn}");`;
};

Blockly.JavaScript['francaster-sleep'] = function (block) {
    var sleepTime = block.getFieldValue("NB_SEC");
    return `runPiRobotCommand("francaster-sleep", "${sleepTime}");`;
};

Blockly.JavaScript['francaster_walk_n_steps'] = function (block) {
    var nb_steps = block.getFieldValue('NB_STEPS');

    return `runPiRobotCommand("francaster-walk_n_steps", "${nb_steps}");`;
};

Blockly.JavaScript['francaster_walk_n_steps_with_knee_lift'] = function (block) {
    var nb_steps = block.getFieldValue('NB_STEPS');

    return `runPiRobotCommand("francaster-walk_n_steps_with_knee_lift", "${nb_steps}");`;
};

Blockly.JavaScript['francaster-do_hi'] = function (block) {
    var value_nb_hi = block.getFieldValue('NB_HI');

    return `runPiRobotCommand("francaster-do_hi", "${value_nb_hi}");`;
};

Blockly.JavaScript['francaster-do_yes'] = function (block) {
    var dropdown_motor = block.getFieldValue('MOVE');
    return dropdown_motor === "o" ? `runPiRobotCommand("francaster-do_yes");` : `runPiRobotCommand("francaster-do_no");`;
};

Blockly.JavaScript['francaster-reset_position'] = function (block) {
    return `runPiRobotCommand("francaster-reset_position");`;
};

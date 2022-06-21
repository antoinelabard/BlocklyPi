Blockly.JavaScript['move'] = function(block) {
  return 'runPiRobotCommand("armController.main")';
};

Blockly.JavaScript['fingers'] = function(block) {
  var dropdown_doigt = block.getFieldValue('doigt');
  switch(dropdown_doigt) {
  case '1':
    code = 'runPiRobotCommand("armController.un")';
    break;
  case '2':
    code = 'runPiRobotCommand("sarmController.deux")';
    break;
  case '3':
	code = 'runPiRobotCommand("sarmController.trois")';
	break;
  
  case '4':
	code = 'runPiRobotCommand("armController.quatre")';
	break;
  
  case '5':
	code = 'runPiRobotCommand("armController.cinq")';
    break;
  default:
    code = 'runPiRobotCommand("armController.main")';
}
  return code;
};


Blockly.JavaScript['main_control'] = function(block) {
  var dropdown_choix = block.getFieldValue('choix');
  switch(dropdown_choix) {
  case 'fermer':
    code = 'runPiRobotCommand("armController.position")';
    break;
  case 'ouvrir':
    code = 'runPiRobotCommand("armController.reset_position")';
    break;
  }
  
  return code;
};

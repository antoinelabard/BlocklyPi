Blockly.JavaScript['move'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  return 'runPiRobotCommand("allbotsController.marcher")';
};

Blockly.JavaScript['fingers'] = function(block) {
  var dropdown_doigt = block.getFieldValue('doigt');
  switch(dropdown_doigt) {
  case '1':
    code = 'runPiRobotCommand("allbotsController.un")';
    break;
  case '2':
    code = 'runPiRobotCommand("allbotsController.deux")';
    break;
  case '3':
	code = 'runPiRobotCommand("allbotsController.trois")';
	break;
  
  case '4':
	code = 'runPiRobotCommand("allbotsController.quatre")';
	break;
  
  case '5':
	code = 'runPiRobotCommand("allbotsController.cinq")';
    break;
  default:
    code = 'runPiRobotCommand("allbotsController.marcher")';
}
  return code;
};


Blockly.JavaScript['rotation_moteur'] = function(block) {
  var dropdown_moteur = block.getFieldValue('moteur');
  var value_angle = Blockly.JavaScript.valueToCode(block, 'angle', Blockly.JavaScript.ORDER_ATOMIC);
  var code = 'runPiRobotCommand("allbotsController.position","' + dropdown_moteur + '",' + value_angle + ');';
  return code;
};

Blockly.JavaScript['incremente_moteur'] = function(block) {
  var dropdown_moteur = block.getFieldValue('moteur');
  var dropdown_choix = block.getFieldValue('choix');
  var value_angle = Blockly.JavaScript.valueToCode(block, 'angle', Blockly.JavaScript.ORDER_ATOMIC);
  if(dropdown_choix == "incremente"){
    var code = 'runPiRobotCommand("allbotsController.plus","' + dropdown_moteur + '",' + value_angle + ');';
  }
  else{
    var code = 'runPiRobotCommand("allbotsController.moins","' + dropdown_moteur + '",' + value_angle + ');';
  }
  
  return code;
};



Blockly.JavaScript['led_on'] = function(block) {
  var dropdown_etat = block.getFieldValue('etat');
  // TODO: Assemble JavaScript into code variable.
  switch(dropdown_etat) {
  case '1':
    code = 'runPiRobotCommand("allbotsController.led_on")';
    break;
  case '2':
    code = 'runPiRobotCommand("allbotsController.led_off")';
    break;
  }
  return code;
};

Blockly.JavaScript['tourner_moteur'] = function(block) {
  var dropdown_moteur = block.getFieldValue('moteur');
  var value_angle = Blockly.JavaScript.valueToCode(block, 'angle', Blockly.JavaScript.ORDER_ATOMIC);
  
  var code = 'runPiRobotCommand("allbotsController.tourne","' + dropdown_moteur + '",' + value_angle + ');';
  
  return code;
};

Blockly.JavaScript['led_clignote'] = function(block) {
  var value_rep = Blockly.JavaScript.valueToCode(block, 'rep', Blockly.JavaScript.ORDER_ATOMIC);
  var dropdown_temps = block.getFieldValue('temps');
  // TODO: Assemble JavaScript into code variable.
  var code = 'runPiRobotCommand("allbotsController.led_clignote","' + value_rep + '",' + dropdown_temps + ');';
  return code;
};


Blockly.JavaScript['bouton'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'runPiRobotCommand("allbotsController.excute")';
  return [code, Blockly.JavaScript.ORDER_NONE];
};

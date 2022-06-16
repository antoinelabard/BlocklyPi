Blockly.JavaScript['move'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  return 'runPiRobotCommand("sensorController.marcher")';
};

Blockly.JavaScript['fingers'] = function(block) {
  var dropdown_doigt = block.getFieldValue('doigt');
  switch(dropdown_doigt) {
  case '1':
    code = 'runPiRobotCommand("sensorController.un")';
    break;
  case '2':
    code = 'runPiRobotCommand("sensorController.deux")';
    break;
  case '3':
	code = 'runPiRobotCommand("sensorController.trois")';
	break;
  
  case '4':
	code = 'runPiRobotCommand("sensorController.quatre")';
	break;
  
  case '5':
	code = 'runPiRobotCommand("sensorController.cinq")';
    break;
  default:
    code = 'runPiRobotCommand("sensorController.marcher")';
}
  return code;
};


Blockly.JavaScript['rotation_moteur'] = function(block) {
  var dropdown_moteur = block.getFieldValue('moteur');
  var value_angle = Blockly.JavaScript.valueToCode(block, 'angle', Blockly.JavaScript.ORDER_ATOMIC);
  var code = 'runPiRobotCommand("sensorController.position","' + dropdown_moteur + '",' + value_angle + ');';
  return code;
};

Blockly.JavaScript['incremente_moteur'] = function(block) {
  var dropdown_moteur = block.getFieldValue('moteur');
  var dropdown_choix = block.getFieldValue('choix');
  var value_angle = Blockly.JavaScript.valueToCode(block, 'angle', Blockly.JavaScript.ORDER_ATOMIC);
  if(dropdown_choix == "incremente"){
    var code = 'runPiRobotCommand("sensorController.plus","' + dropdown_moteur + '",' + value_angle + ');';
  }
  else{
    var code = 'runPiRobotCommand("sensorController.moins","' + dropdown_moteur + '",' + value_angle + ');';
  }
  
  return code;
};



Blockly.JavaScript['led_on'] = function(block) {
  var dropdown_etat = block.getFieldValue('etat');
  // TODO: Assemble JavaScript into code variable.
  switch(dropdown_etat) {
  case '1':
    code = 'runPiRobotCommand("sensorController.led_on")';
    break;
  case '2':
    code = 'runPiRobotCommand("sensorController.led_off")';
    break;
  }
  return code;
};

Blockly.JavaScript['tourner_moteur'] = function(block) {
  var dropdown_moteur = block.getFieldValue('moteur');
  var value_angle = Blockly.JavaScript.valueToCode(block, 'angle', Blockly.JavaScript.ORDER_ATOMIC);
  
  var code = 'runPiRobotCommand("sensorController.tourne","' + dropdown_moteur + '",' + value_angle + ');';
  
  return code;
};

Blockly.JavaScript['led_clignote'] = function(block) {
  var value_rep = Blockly.JavaScript.valueToCode(block, 'rep', Blockly.JavaScript.ORDER_ATOMIC);
  var dropdown_temps = block.getFieldValue('temps');
  // TODO: Assemble JavaScript into code variable.
  var code = 'runPiRobotCommand("sensorController.led_clignote","' + value_rep + '",' + dropdown_temps + ');';
  return code;
};


Blockly.JavaScript['bouton'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'runPiRobotCommand("sensorController.excute")';
  return [code, Blockly.JavaScript.ORDER_NONE];
};


Blockly.JavaScript['repos'] = function(block) {
  var dropdown_temps = block.getFieldValue('temps');
  // TODO: Assemble JavaScript into code variable.
  var code = 'runPiRobotCommand("sensorController.repos","' + dropdown_temps + ');';
  return code;
};





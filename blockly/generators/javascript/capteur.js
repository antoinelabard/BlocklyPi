

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
  var code = 'runPiRobotCommand("sensorController.bouton")';
  return [code, Blockly.JavaScript.ORDER_NONE];
};


Blockly.JavaScript['repos'] = function(block) {
  var dropdown_temps = block.getFieldValue('temps');
  // TODO: Assemble JavaScript into code variable.
  var code = 'runPiRobotCommand("sensorController.repos","' + dropdown_temps + ');';
  return code;
};


Blockly.JavaScript['distance'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'runPiRobotCommand("sensorController.distance")';
  return code;
};


Blockly.JavaScript['moteur_avec_potentiometre'] = function(block) {
  var dropdown_moteur = block.getFieldValue('moteur');
  // TODO: Assemble JavaScript into code variable.
  var code = 'runPiRobotCommand("sensorController.moteur_potentiometre","' + dropdown_moteur + ');';
  return code;
};



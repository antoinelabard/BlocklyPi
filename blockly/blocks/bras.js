Blockly.Blocks['move'] = {
  init: function() {
    this.appendDummyInput()
        .setAlign(Blockly.ALIGN_CENTRE)
        .appendField("Bouger la main");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(160);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['fingers'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("choisit un chiffre")
        .appendField(new Blockly.FieldDropdown([["1","1"], ["2","2"], ["3","3"], ["4","4"], ["5","5"]]), "doigt");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(160);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['rotation_moteur'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Mettre le moteur : ")
        .appendField(new Blockly.FieldDropdown([["0","a"], ["1","b"], ["2","c"], ["3","d"], ["4","e"], ["5","f"], ["6","g"], ["7","h"], ["8","i"], ["9","j"], ["10","k"], ["11","l"], ["12","m"], ["13","n"], ["14","o"], ["15","p"]]), "moteur")
        .appendField("à la position : ");
    this.appendValueInput("angle")
        .setCheck("Number");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(160);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['incremente_moteur'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([["incrementer","incremente"], ["decrementer","decremente"]]), "choix")
        .appendField("le moteur : ")
        .appendField(new Blockly.FieldDropdown([["0","a"], ["1","b"], ["2","c"], ["3","d"], ["4","e"], ["5","f"], ["6","g"], ["7","h"], ["8","i"], ["9","j"], ["10","k"], ["11","l"], ["12","m"], ["13","n"], ["14","o"], ["15","p"]]), "moteur")
        .appendField("de : ");
    this.appendValueInput("angle")
        .setCheck("Number");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(160);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['led_on'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Led : ")
        .appendField(new Blockly.FieldDropdown([["On","1"], ["Off","2"]]), "etat");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['tourner_moteur'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Tourner le moteur : ")
        .appendField(new Blockly.FieldDropdown([["0","a"], ["1","b"], ["2","c"], ["3","d"], ["4","e"], ["5","f"], ["6","g"], ["7","h"], ["8","i"], ["9","j"], ["10","k"], ["11","l"], ["12","m"], ["13","n"], ["14","o"], ["15","p"]]), "moteur")
        .appendField("de : ");
    this.appendValueInput("angle")
        .setCheck("Number");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(160);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['led_clignote'] = {
  init: function() {
    this.appendValueInput("rep")
        .setCheck("Number")
        .appendField("Clignoter la led");
    this.appendDummyInput()
        .appendField("fois a une vitesse:")
        .appendField(new Blockly.FieldDropdown([["Très élevé","0.1"], ["Elevé","0.2"], ["Moyenne","0.3"], ["Faible","0.5"], ["Très faible","1"]]), "temps");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(160);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};





Blockly.Blocks['bouton'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("bouton");
    this.setOutput(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

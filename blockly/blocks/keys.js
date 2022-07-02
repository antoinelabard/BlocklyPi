Blockly.Blocks['control_key_down'] = {
    init: function () {
        this.setHelpUrl('http://www.example.com/');
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(210);
        this.appendDummyInput()
        .appendField("Si la touche")
        .appendField(new Blockly.FieldDropdown([
            ["↓", "DOWN"], ["↑", "UP"],
            ["←", "LEFT"], ["→", "RIGHT"],
            ["a", "a"], ["b", "b"], 
            ["c", "c"], ["d", "d"], 
            ["e", "e"], ["f", "f"], 
            ["g", "g"], ["h", "h"], 
            ["i", "i"], ["j", "j"], 
            ["k", "k"], ["l", "l"], 
            ["m", "m"], ["n", "n"], 
            ["o", "o"], ["p", "p"], 
            ["q", "q"], ["r", "r"], 
            ["s", "s"], ["t", "t"], 
            ["u", "u"], ["v", "v"], 
            ["w", "w"], ["x", "x"], 
            ["y", "y"], ["z", "z"],
            ["0", "0"], ["1", "1"],
            ["2", "2"], ["3", "3"],
            ["4", "4"], ["5", "5"],
            ["6", "6"], ["7", "7"],
            ["8", "8"], ["9", "9"], ]), "KEY")
            .appendField("est presseé");

        this.appendStatementInput("STATEMENTS");
        this.setTooltip('');
    }
};

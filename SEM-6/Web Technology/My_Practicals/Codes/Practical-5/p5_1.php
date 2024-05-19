<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- GIVE ME A USER INTERACTIVE FORM IN WHICH USING THE INPUT FROM SELECET MENU I CHOOSE TO PERFORM PARTICULAR OPERATION ON STRING TAKEN FROM INPUT AND FOR PARTICULAR INPUT THE CUSTOMISED BUTTON SHOWS AND OUTPUT COMES AFTER PRESSING THE BUTTON AND MAKE THE WHOLE FORM AT CENTER -->
    <form action="" method="post">
        <label for="string">Enter the string:</label>
        <input type="text" name="string" id="string">
        <br>
        <label for="operation">Choose the operation:</label>
        <select name="operation" id="operation">
            <option value="length">Length of the string</option>
            <option value="lower">Convert to Lowercase</option>
            <option value="upper">Convert to Uppercase</option>
            <option value="whitespace">Count Whitespace</option>
            <option value="wordsLinesCharacters">Count Words, Lines and Characters</option>
            <option value="position">Position of a word</option>
            <option value="replace">Replace a word</option>
            <option value="vowels">Count Occurences of Vowels</option>
        </select>
        <br>
        <input type="submit" value="Submit">
    </form>
    
</body>
</html>
<?php
        if(isset($_POST['string'])){
            $str = $_POST['string'];
            $operation = $_POST['operation'];
            switch($operation){
                case "length":
                    echo "Length of the string is ".findLength($str);
                    break;
                case "lower":
                    echo "String in Lowercase is ".toLower($str);
                    break;
                case "upper":
                    echo "String in Uppercase is ".toUpper($str);
                    break;
                case "whitespace":
                    echo "No of Whitespace in the string is ".countWhitespace($str);
                    break;
                case "wordsLinesCharacters":
                    countWordsLinesCharacters($str);
                    break;
                case "position":
                    echo "Position of the word is ".positionOfWord($str,"word");
                    break;
                case "replace":
                    echo "String after replacing the word is ".replaceWord($str,"oldWord","newWord");
                    break;
                case "vowels":
                    echo "No of Vowels in the string is ".occurencesOfVowels($str);
                    break;
            }
        }
?>

<!-- 
    if (isset($_POST['string'])) {
    $str = $_POST['string'];
    $operation = $_POST['operation'];

    if ($operation == 'length') {
        echo "Length of the string is " . findLength($str);
    } else if ($operation == 'lower') {
        echo "String in Lowercase is " . toLower($str);
    } else if ($operation == 'upper') {
        echo "String in Uppercase is " . toUpper($str);
    } else if ($operation == 'whitespace') {
        echo "No of Whitespace in the string is " . countWhitespace($str);
    } else if ($operation == 'wordsLinesCharacters') {
        countWordsLinesCharacters($str);
    } else if ($operation == 'position') {
        echo "Position of the word is " . positionOfWord($str, "word");
    } else if ($operation == 'replace') {
        echo "String after replacing the word is " . replaceWord($str, "oldWord", "newWord");
    } else if ($operation == 'vowels') {
        echo "No of Vowels in the string is " . occurencesOfVowels($str);
    }
}
 -->
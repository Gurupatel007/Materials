<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body{
            font-family: Rubik, sans-serif;
            font-weight: 700;
        }
        .contianer {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background-color: #fff;
            border-radius: 10px;
            height: 100vh;
            

        }
        
        .form {
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            box-shadow: 0 0 30px #ccc;
            width: 500px;
            border-radius: 30px;
            background-color: #fff;
            box-shadow: 0px 4px 6px -1px rgba(0, 0, 0, 0.1), 0px 0px 6px 0px rgba(0, 0, 0, 0.1);
        }
        
        form {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        input[type="text"],
        select {
            padding: 10px;
            margin: 10px;
            width: 300px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        input[type="submit"] {
            padding: 10px;
            margin: 10px;
            width: 100px;
            border-radius: 5px;
            border: 1px solid #ccc;
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
            font-size: 16px;
            font-weight: 800;
        }

        input[type="submit"]:hover {
            background-color: #45a049;
        }

        .repword {
            display: none;
        }
        .wordPosi{
            display: none;
        }

        .output {
            margin-top: 20px;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px #ccc;
            background-color: #fff;
            box-shadow: 0px 4px 6px -1px rgba(0, 0, 0, 0.1), 0px 0px 6px 0px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>

<body>
    <div class="contianer">
        <div class="form">
            <form action="" method="post">
            <h1>String Operations</h1>
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
                <input type="text" name="wordPosition" id="wordPosition" class="wordPosi" placeholder="Enter the Word">
                <br>
                <input type='text' name='oldWord' id='oldWord' class="repword" placeholder="Old word">
                <br>
                <input type='text' name='newWord' id='newWord' class="repword" placeholder="New word">
                <br><br>
                <script>
                    document.getElementById('operation').addEventListener('change', function() {
                        var operation = document.getElementById('operation').value;
                        if (operation == 'replace') {
                            document.getElementById('oldWord').style.display = 'block';
                            document.getElementById('newWord').style.display = 'block';
                        } else {
                            document.getElementById('oldWord').style.display = 'none';
                            document.getElementById('newWord').style.display = 'none';
                        }
                        var operation = document.getElementById('operation').value;
                        if (operation == 'position') {
                            document.getElementById('wordPosition').style.display = 'block';
                        } else {
                            document.getElementById('wordPosition').style.display = 'none';
                        }
                    });
                    // document.getElementById('operation').addEventListener('change', function() {
                    //     var operation = document.getElementById('operation').value;
                    //     if (operation == 'position') {
                    //         document.getElementById('wordPosition').style.display = 'block';
                    //     } else {
                    //         document.getElementById('wordPosition').style.display = 'none';
                    //     }
                    // });
                </script>
                <input type="submit" value="Submit">
            </form>
        </div>
        <div class="output">
            <?php
            if (isset($_POST['string'])) {
                $str = $_POST['string'];
                $operation = $_POST['operation'];

                switch ($operation) {
                    case "length":
                        echo "Length of the string is <b>" . findLength($str)."</b>";
                        break;
                    case "lower":
                        echo "String in Lowercase is <b>" . toLower($str)."</b>";
                        break;
                    case "upper":
                        echo "String in Uppercase is <b>" . toUpper($str)."</b>";
                        break;
                    case "whitespace":
                        echo "No of Whitespace in the string is <b>" . countWhitespace($str)."</b>";
                        break;
                    case "wordsLinesCharacters":
                        countWordsLinesCharacters($str);
                        break;
                    case "position":
                        $word = $_POST['wordPosition'];
                        echo "Position of the word is <b>" . positionOfWord($str, $word)."</b>";
                        break;
                    case "replace":
                        $oldWord = $_POST['oldWord'];
                        $newWord = $_POST['newWord'];
                        echo "String after replacing the word is '<b>" . replaceWord($str, $oldWord, $newWord)."</b>'";
                        break;
                    case
                    "vowels":
                        echo "No of Vowels in the string is <b>" . occurencesOfVowels($str)."</b>";
                        break;
                }
            }
            ?>
        </div>
    </div>
</body>

</html>
<?php
function findLength($str)
{
    return strlen($str);
}

function toLower($str)
{
    return strtolower($str);
}
function toUpper($str)
{
    return strtoupper($str);
}
function countWhitespace($str)
{
    return substr_count($str, " ");
}
function countWordsLinesCharacters($str)
{
    $words = str_word_count($str);
    $lines = substr_count($str, "\n");
    $characters = strlen($str);

    echo "No of Words :$words<br>";
    echo "No of Lines :" . ($lines + 1) . "<br>";
    echo "No of characters: $characters<br>";
}
function positionOfWord($str, $word)
{
    return strpos($str, $word);
}
function replaceWord($str, $oldWord, $newWord)
{
    return str_replace($oldWord, $newWord, $str);
}
function occurencesOfVowels($str)
{
    $count = preg_match_all('/[aeiou]/i', $str);
    return $count;
}
?>
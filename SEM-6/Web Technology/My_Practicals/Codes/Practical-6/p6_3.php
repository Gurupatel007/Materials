<!-- 3. Develop functionality to manage uploaded files:
a. List uploaded files with options for viewing, downloading, or 
deleting them.
 -->
<!DOCTYPE html>
<html>
    <head>
        <title>File Upload</title>
        <style>
            table{
                width: 100%;
                border-collapse: collapse;
            }
            table, th, td{
                border: 1px solid black;
            }
            th, td{
                padding: 10px;
                text-align: left;
            }
            th{
                background-color: #f2f2f2;
            }

        </style>
    </head>
    <body>
        <form action="p6_3.php" method="post" enctype="multipart/form-data">
            <input type="file" name="file" id="file">
            <input type="submit" value="Upload" name="submit">
        </form>
        <?php
            if(isset($_POST['submit'])){
                $file = $_FILES['file'];
                $fileName = $_FILES['file']['name'];
                $fileTmpName = $_FILES['file']['tmp_name'];
                $fileSize = $_FILES['file']['size'];
                $fileError = $_FILES['file']['error'];
                $fileType = $_FILES['file']['type'];

                $fileExt = explode('.',$fileName);
                $fileActualExt = strtolower(end($fileExt));

                $allowed = array('jpg','jpeg','png','pdf');

                if(in_array($fileActualExt,$allowed)){
                    if($fileError === 0){
                        if($fileSize < 1000000){
                            $fileNameNew = uniqid('',true).".".$fileActualExt;
                            $fileDestination = 'uploads/'.$fileNameNew;
                            move_uploaded_file($fileTmpName,$fileDestination);
                            echo "File uploaded successfully";
                        }
                        else{
                            echo "File size is too large";
                        }
                    }
                    else{
                        echo "Error uploading file";
                    }
                }
                else{
                    echo "Invalid file type";
                }
            }
        ?>
        <br>
        <h2>Uploaded Files</h2>
        <table>
            <tr>
                <th>File Name</th>
                <th>View</th>
                <th>Download</th>
                <th>Delete</th>
            </tr>
            <?php
                $dir = "uploads/";
                $files = scandir($dir);
                foreach($files as $file){
                    if($file != '.' && $file != '..'){
                        echo "<tr>";
                        echo "<td>".$file."</td>";
                        echo "<td><a href='uploads/".$file."' target='_blank'>View</a></td>";
                        echo "<td><a href='uploads/".$file."' download>Download</a></td>";
                        echo "<td><a href='delete.php?file=".$file."'>Delete</a></td>";
                        echo "</tr>";
                    }

                }
            ?>
        </table>
    </body>
</html>
<!-- // Output:
// File uploaded successfully
// Uploaded Files
// File Name	View	Download	Delete
// 5f6b3b3b1e7b38.2020-09-23 12:00:59.jpg	View	Download	Delete -->
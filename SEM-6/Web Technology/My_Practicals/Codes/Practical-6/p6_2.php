<!-- 2. Create a form with a file input field to allow users to upload files.
Implement server-side PHP code to handle the uploaded file:
a. Validate the file type and size to prevent malicious uploads and 
ensure server resource management.
b. Move the uploaded file to a secure location on the server.
c. Provide feedback to the user on the success or failure of the 
upload process. -->
<!DOCTYPE html>
<html>
    <head>
        <title>File Upload</title>
    </head>
    <body>
        <form action="p6_2.php" method="post" enctype="multipart/form-data">
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
    </body>
</html>
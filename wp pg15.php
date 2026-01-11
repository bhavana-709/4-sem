<!DOCTYPE html>
<html>
  <head>
    <title>File Reader and Writer</title>
  </head>
  <body>
    <h1>Write to a File</h1>
    <form action="FileReadWrite.php" method="post">
      <label for="textdata">Enter Text:</label><br />
      <textarea name="textdata" id="textdata" rows="5" cols="40"></textarea
      ><br /><br />
      <input type="submit" value="Write to File" />
    </form>

    <h1>Read Uploaded File</h1>
    <form
      action="FileReadWrite.php"
      method="post"
      enctype="multipart/form-data"
    >
      <label for="filedata">Upload File to Read Contents:</label><br />
      <input type="file" name="filedata" id="filedata" /><br /><br />
      <input type="submit" value="Read File Contents" />
    </form>
  </body>
</html>

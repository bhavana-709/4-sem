<?php
// Start the session
session_start();

// Connect to the database
$conn = new mysqli("localhost", "root", "", "myDB"); // Update credentials if needed

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// If an image is requested via GET
if (isset($_GET['id'])) {
    $id = intval($_GET['id']);
    $stmt = $conn->prepare("SELECT image_type, image_data FROM images WHERE id = ?");
    $stmt->bind_param("i", $id);
    $stmt->execute();
    $stmt->bind_result($imageType, $imageData);
    $stmt->fetch();
    $stmt->close();

    header("Content-Type: $imageType");
    echo $imageData;
    exit;
}

// If image is uploaded via POST
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_FILES["image"])) {
    $imageData = file_get_contents($_FILES["image"]["tmp_name"]);
    $imageName = $_FILES["image"]["name"];
    $imageType = $_FILES["image"]["type"];

    $stmt = $conn->prepare("INSERT INTO images (image_name, image_type, image_data) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $imageName, $imageType, $imageData);
    $stmt->execute();
    $stmt->close();
}

// Function to display all uploaded images
function displayImages($conn) {
    $sql = "SELECT id, image_name FROM images";
    $result = $conn->query($sql);

    while ($row = $result->fetch_assoc()) {
        echo "<p><strong>" . htmlspecialchars($row["image_name"]) . "</strong><br>";
        echo "<img src='?id=" . $row["id"] . "' alt='" . htmlspecialchars($row["image_name"]) . "' style='max-width:300px;'><br><br></p>";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Image Upload and Display</title>
</head>
<body>
    <h1>Upload and Display Images</h1>
    <form method="post" enctype="multipart/form-data">
        Select image to upload: <br>
        <input type="file" name="image" id="image"><br><br>
        <input type="submit" value="Upload Image" name="submit">
    </form>

    <h2>Uploaded Images:</h2>
    <?php displayImages($conn); ?>
    <?php $conn->close(); ?>
</body>
</html>

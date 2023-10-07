<?php
// Establish a database connection (you'll need to replace these with your actual database credentials)
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "web_sql";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Process form 
$firstname = $_POST['firstname'];
$lastname= $_POST['lastname'];
$username = $_POST['username'];
$password = $_POST['password'];
$email = $_POST['email'];

// Insert data into the database
$sql = "INSERT INTO user (firstname, lastname, username, password, email) VALUES ('$firstname','$lastname','$username', '$password', '$email')";

if ($conn->query($sql) === TRUE) {
    echo "Data inserted successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>

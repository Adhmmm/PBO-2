<?php
require_once 'database.php';
require_once 'Mhspinjam.php';
$db = new MySQLDatabase();
$mhspinjam = new Mhspinjam($db);
$id=0;
$ida=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['ida'])){
            $ida = $_GET['ida'];
        }
        if($id>0){    
            $result = $mhspinjam->get_by_id($id);
        }elseif($ida>0){
            $result = $mhspinjam->get_by_ida($ida);
        } else {
            $result = $mhspinjam->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new mhspinjam
        $mhspinjam->kodebuku = $_POST['kodebuku'];
        $mhspinjam->ida = $_POST['ida'];
        $mhspinjam->nama = $_POST['nama'];
        $mhspinjam->jk = $_POST['jk'];
        $mhspinjam->alamat = $_POST['alamat'];
        $mhspinjam->buku = $_POST['buku'];
        $mhspinjam->peminjaman = $_POST['peminjaman'];
        $mhspinjam->pengembalian = $_POST['pengembalian'];
       
        $mhspinjam->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Mhspinjam created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Mhspinjam not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['ida'])){
            $ida = $_GET['ida'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $mhspinjam->kodebuku = $_PUT['kodebuku'];
        $mhspinjam->ida = $_PUT['ida'];
        $mhspinjam->nama = $_PUT['nama'];
        $mhspinjam->jk = $_PUT['jk'];
        $mhspinjam->alamat = $_PUT['alamat'];
        $mhspinjam->buku = $_PUT['buku'];
        $mhspinjam->peminjaman = $_PUT['peminjaman'];
        $mhspinjam->pengembalian = $_PUT['pengembalian'];
        if($id>0){    
            $mhspinjam->update($id);
        }elseif($ida<>""){
            $mhspinjam->update_by_ida($ida);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Mhspinjam updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Mhspinjam update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['ida'])){
            $ida = $_GET['ida'];
        }
        if($id>0){    
            $mhspinjam->delete($id);
        }elseif($ida>0){
            $mhspinjam->delete_by_ida($ida);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Mhspinjam deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Mhspinjam delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>
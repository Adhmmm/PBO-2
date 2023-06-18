<?php
require_once 'database.php';
require_once 'Peminjaman.php';
$db = new MySQLDatabase();
$peminjaman = new Peminjaman($db);
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
            $result = $peminjaman->get_by_id($id);
        }elseif($ida>0){
            $result = $peminjaman->get_by_ida($ida);
        } else {
            $result = $peminjaman->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new peminjaman
        $peminjaman->kodebuku = $_POST['kodebuku'];
        $peminjaman->ida = $_POST['ida'];
        $peminjaman->nama = $_POST['nama'];
        $peminjaman->jk = $_POST['jk'];
        $peminjaman->alamat = $_POST['alamat'];
        $peminjaman->buku = $_POST['buku'];
        $peminjaman->tahunterbit = $_POST['tahunterbit'];
        $peminjaman->kategori = $_POST['kategori'];
        $peminjaman->penulis = $_POST['penulis'];
        $peminjaman->penerbit = $_POST['penerbit'];
        $peminjaman->peminjaman = $_POST['peminjaman'];
        $peminjaman->pengembalian = $_POST['pengembalian'];
        $peminjaman->telat = $_POST['telat'];
        $peminjaman->denda = $_POST['denda'];
       
        $peminjaman->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman not created.';
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
        $peminjaman->kodebuku = $_PUT['kodebuku'];
        $peminjaman->ida = $_PUT['ida'];
        $peminjaman->nama = $_PUT['nama'];
        $peminjaman->jk = $_PUT['jk'];
        $peminjaman->alamat = $_PUT['alamat'];
        $peminjaman->buku = $_PUT['buku'];
        $peminjaman->tahunterbit = $_PUT['tahunterbit'];
        $peminjaman->kategori = $_PUT['kategori'];
        $peminjaman->penulis = $_PUT['penulis'];
        $peminjaman->penerbit = $_PUT['penerbit'];
        $peminjaman->peminjaman = $_PUT['peminjaman'];
        $peminjaman->pengembalian = $_PUT['pengembalian'];
        $peminjaman->telat = $_PUT['telat'];
        $peminjaman->denda = $_PUT['denda'];
        if($id>0){    
            $peminjaman->update($id);
        }elseif($ida<>""){
            $peminjaman->update_by_ida($ida);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman update failed.';
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
            $peminjaman->delete($id);
        }elseif($ida>0){
            $peminjaman->delete_by_ida($ida);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman delete failed.';
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
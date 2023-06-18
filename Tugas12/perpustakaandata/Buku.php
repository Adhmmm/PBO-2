<?php
//Simpanlah dengan nama file : Buku.php
require_once 'database.php';
class Buku 
{
    private $db;
    private $table = 'buku';
    public $kodebuku = "";
    public $buku = "";
    public $penulis = "";
    public $penerbit = "";
    public $tahun = "";
    public $kategori = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_kodebuku(int $kodebuku)
    {
        $query = "SELECT * FROM $this->table WHERE kodebuku = $kodebuku";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kodebuku`,`buku`,`penulis`,`penerbit`,`tahun`,`kategori`) VALUES ('$this->kodebuku','$this->buku','$this->penulis','$this->penerbit','$this->tahun','$this->kategori')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kodebuku = '$this->kodebuku', buku = '$this->buku', penulis = '$this->penulis', penerbit = '$this->penerbit', tahun = '$this->tahun', kategori = '$this->kategori' 
        WHERE idbk = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kodebuku($kodebuku): int
    {
        $query = "UPDATE $this->table SET kodebuku = '$this->kodebuku', buku = '$this->buku', penulis = '$this->penulis', penerbit = '$this->penerbit', tahun = '$this->tahun', kategori = '$this->kategori' 
        WHERE kodebuku = $kodebuku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE idbk = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kodebuku($kodebuku): int
    {
        $query = "DELETE FROM $this->table WHERE kodebuku = $kodebuku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>
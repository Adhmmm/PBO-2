<?php
//Simpanlah dengan nama file : Peminjaman.php
require_once 'database.php';
class Peminjaman 
{
    private $db;
    private $table = 'peminjaman';
    public $kodebuku = "";
    public $ida = "";
    public $nama = "";
    public $jk = "";
    public $alamat = "";
    public $buku = "";
    public $tahunterbit = "";
    public $kategori = "";
    public $penulis = "";
    public $penerbit = "";
    public $peminjaman = "";
    public $pengembalian = "";
    public $telat = "";
    public $denda = "";
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
    public function get_by_ida(int $ida)
    {
        $query = "SELECT * FROM $this->table WHERE ida = $ida";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kodebuku`,`ida`,`nama`,`jk`,`alamat`,`buku`,`tahunterbit`,`kategori`,`penulis`,`penerbit`,`peminjaman`,`pengembalian`,`telat`,`denda`) VALUES ('$this->kodebuku','$this->ida','$this->nama','$this->jk','$this->alamat','$this->buku','$this->tahunterbit','$this->kategori','$this->penulis','$this->penerbit','$this->peminjaman','$this->pengembalian','$this->telat','$this->denda')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kodebuku = '$this->kodebuku', ida = '$this->ida', nama = '$this->nama', jk = '$this->jk', alamat = '$this->alamat', buku = '$this->buku', tahunterbit = '$this->tahunterbit', kategori = '$this->kategori', penulis = '$this->penulis', penerbit = '$this->penerbit', peminjaman = '$this->peminjaman', pengembalian = '$this->pengembalian', telat = '$this->telat', denda = '$this->denda' 
        WHERE idprsp = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_ida($ida): int
    {
        $query = "UPDATE $this->table SET kodebuku = '$this->kodebuku', ida = '$this->ida', nama = '$this->nama', jk = '$this->jk', alamat = '$this->alamat', buku = '$this->buku', tahunterbit = '$this->tahunterbit', kategori = '$this->kategori', penulis = '$this->penulis', penerbit = '$this->penerbit', peminjaman = '$this->peminjaman', pengembalian = '$this->pengembalian', telat = '$this->telat', denda = '$this->denda' 
        WHERE ida = $ida";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE idprsp = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_ida($ida): int
    {
        $query = "DELETE FROM $this->table WHERE ida = $ida";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>
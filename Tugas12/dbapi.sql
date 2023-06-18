-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 18, 2023 at 22:45 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbapi`
--

-- --------------------------------------------------------

--
-- Table structure for table `Buku`
--

CREATE TABLE `Buku` (
  `idbk` int(10) NOT NULL,
  `kodebuku` int(10) NOT NULL,
  `buku` varchar(50) NOT NULL,
  `penulis` varchar(50) NOT NULL,
  `penerbit` varchar(50) NOT NULL,
  `tahun` varchar(10) NOT NULL,
  `kategori` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `buku`
--

INSERT INTO `Buku` (`idbk`, `kodebuku`, `buku`, `penulis`, `penerbit`, `tahun`, `kategori`) VALUES
(1, 202301, 'Cara Ngoding', 'Jono', 'Yanto', '2009', 'Ensiklopedia'),
(2, 202302, 'Kamus Bahasa Spanyol', 'Jono', 'Yanto', '2012', 'Ensiklopedia'),
(3, 202303, 'Dilan 1991', 'Jono', 'Yanto', '2020', 'Ensiklopedia');

-- --------------------------------------------------------

--
-- Table structure for table `mhspinjam`
--

CREATE TABLE `mhspinjam` (
  `idprsp` int(15) NOT NULL,
  `kodebuku` int(10) NOT NULL,
  `ida` int(10) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `jk` varchar(10) NOT NULL,
  `alamat` varchar(20) NOT NULL,
  `buku` varchar(50) NOT NULL,
  `peminjaman` varchar(50) NOT NULL,
  `pengembalian` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mhspinjam`
--

INSERT INTO `mhspinjam` (`idprsp`, `kodebuku`, `ida`, `nama`, `jk`, `alamat`, `buku`, `peminjaman`, `pengembalian`) VALUES
(1, 202301, 210511011, 'Rizki', 'Laki-Laki', 'Palimanan', 'Cara Ngoding', '23 September 2023', '25 September 2023'),
(2, 202302, 210511031, 'Barel', 'Laki-Laki', 'Majalengka', 'Kamus Bahasa Spanyol', '23 September 2023', '25 September 2023'),
(3, 202303, 210511029, 'Silvia', 'Perempuan', 'Pilang', 'Dilan 1991', '23 September 2023', '25 September 2023');

-- --------------------------------------------------------

--
-- Table structure for table `peminjaman`
--

CREATE TABLE `peminjaman` (
  `idprsp` int(15) NOT NULL,
  `kodebuku` int(10) NOT NULL,
  `ida` int(10) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `jk` varchar(10) NOT NULL,
  `alamat` varchar(20) NOT NULL,
  `buku` varchar(50) NOT NULL,
  `tahunterbit` varchar(10) NOT NULL,
  `kategori` varchar(50) NOT NULL,
  `penulis` varchar(50) NOT NULL,
  `penerbit` varchar(50) NOT NULL,
  `peminjaman` varchar(50) NOT NULL,
  `pengembalian` varchar(50) NOT NULL,
  `telat` varchar(20) NOT NULL,
  `denda` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `peminjaman`
--

INSERT INTO `peminjaman` (`idprsp`, `kodebuku`, `ida`, `nama`, `jk`, `alamat`, `buku`, `tahunterbit`, `kategori`, `penulis`, `penerbit`, `peminjaman`, `pengembalian`, `telat`, `denda`) VALUES
(1, 202301, 210511011, 'Rizki', 'Laki-Laki', 'Palimanan', 'Cara Ngoding', '2009', 'Ensiklopedia', 'Jono', 'Yanto', '23 September 2023', '25 September 2023', 'Telat', 'Rp 2.000'),
(2, 202302, 210511031, 'Barel', 'Laki-Laki', 'Majalengka', 'Kamus Bahasa Spanyol', '2012', 'Kamus', 'Jono', 'Yanto', '23 September 2023', '25 September 2023', 'Tidak Telat', 'Rp 0'),
(3, 202303, 210511029, 'Silvia', 'Perempuan', 'Pilang', 'Dilan 1991', '2020', 'Komik', 'Jono', 'Yanto', '23 September 2023', '25 September 2023v', 'Telat', 'Rp 4.000');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `passwd` varchar(50) NOT NULL,
  `rolename` enum('admin','dosen','mahasiswa') NOT NULL DEFAULT 'mahasiswa'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `passwd`, `rolename`) VALUES
(1, 'rizki', '202cb962ac59075b964b07152d234b70', 'admin'),
(2, 'sokid', '202cb962ac59075b964b07152d234b70', 'dosen'),
(3, 'silvia', '202cb962ac59075b964b07152d234b70', 'mahasiswa');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Buku`
--
ALTER TABLE `Buku`
  ADD PRIMARY KEY (`idbk`),
  ADD UNIQUE KEY `kodebuku` (`kodebuku`);

--
-- Indexes for table `mhspinjam`
--
ALTER TABLE `mhspinjam`
  ADD PRIMARY KEY (`idprsp`),
  ADD UNIQUE KEY `ida` (`ida`),
  ADD UNIQUE KEY `kodebuku` (`kodebuku`);

--
-- Indexes for table `peminjaman`
--
ALTER TABLE `peminjaman`
  ADD PRIMARY KEY (`idprsp`),
  ADD UNIQUE KEY `ida` (`ida`),
  ADD UNIQUE KEY `kodebuku` (`kodebuku`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `idx` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `buku`
--
ALTER TABLE `Buku`
  MODIFY `idbk` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `mhspinjam`
--
ALTER TABLE `mhspinjam`
  MODIFY `idprsp` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `peminjaman`
--
ALTER TABLE `peminjaman`
  MODIFY `idprsp` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `mhspinjam`
--
ALTER TABLE `mhspinjam`
  ADD CONSTRAINT `mhspinjam_ibfk_1` FOREIGN KEY (`kodebuku`) REFERENCES `buku` (`kodebuku`);

--
-- Constraints for table `peminjaman`
--
ALTER TABLE `peminjaman`
  ADD CONSTRAINT `peminjaman_ibfk_1` FOREIGN KEY (`kodebuku`) REFERENCES `mhspinjam` (`kodebuku`),
  ADD CONSTRAINT `peminjaman_ibfk_2` FOREIGN KEY (`ida`) REFERENCES `mhspinjam` (`ida`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

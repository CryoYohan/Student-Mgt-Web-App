-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 01, 2024 at 08:56 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `users`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `idno` int(11) NOT NULL,
  `isbn` varchar(10) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `author` varchar(100) DEFAULT NULL,
  `copyright` varchar(50) DEFAULT NULL,
  `edition` varchar(50) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`idno`, `isbn`, `title`, `author`, `copyright`, `edition`, `price`, `qty`, `total`) VALUES
(1, '1001', 'The Sea Wolf', 'Jack London', 'Copyright 1904 by Jack London', 'Bantam Classic', 4.95, 1, 4.95),
(2, '1002', 'Fourth Wing', 'Rebecca Yarros', 'Copyright 2023 by Rebecca Yarros', 'Special Edition', 47.97, 1, 47.97),
(4, '1003', 'Python Distilled', 'David Beazley', 'Copyright 2021 by David Beazley', '1st Edition', 43.20, 3, 129.60),
(6, '1004', 'deep learning', 'Yoshua Bengio', 'Copyright 2015 by Yoshua Bengio', '1st Edition', 107.88, 0, 0.00),
(9, '3333', 'The Jungle Book', 'Mowgli III', 'Copyright 2021', 'Jungle Edition', 22.00, 2, 44.00);

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `idno` varchar(20) DEFAULT NULL,
  `lastname` varchar(55) DEFAULT NULL,
  `firstname` varchar(55) DEFAULT NULL,
  `midinit` varchar(20) DEFAULT NULL,
  `course` varchar(20) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `username` varchar(55) DEFAULT NULL,
  `password_plain` varchar(255) DEFAULT NULL,
  `password_hash` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `idno`, `lastname`, `firstname`, `midinit`, `course`, `level`, `username`, `password_plain`, `password_hash`) VALUES
(5, '1001', 'ypil', 'Kryllos Joe', 'Jehovah   ', 'BSCS', 3, 'tu-1001', '1001-y', '$2b$12$hSCVARM4i8xwAw44ePXGVencZnzy3mj/SBwPQGoVRbsFUBzZAymz6'),
(8, '1002', 'napisa', 'Marianne Joy', 'magsaysay       ', 'bsit', 3, 'tu-1002', '1002-N', '$2b$12$bQMjh9uV/9gIzrPwavOTd.YLCjEBonBaZct4VSl9OZ2LUc/58tozG'),
(10, '1003', 'Magsayo', 'Henrykeen', 'magsaysay      ', 'bsit', 3, 'tu-1003', '1003-m', '$2b$12$BPXTSBbmK8bH1qxRW1E79ONGowPBzIaGYvqYpq5XJAKOsHT5R6Btu'),
(13, '1004', 'Rabanes', 'Jeannel Mia', 'Delinia', 'BSN', 1, 'tu-1004', '1004-r', '$2b$12$6ZjJ0vTrqGFXQQre03aUme4Y8fHGi0WQFfg74c.QRHKsGt39sqDB6'),
(14, '1005', 'Ypil', 'Kryllos Joe', 'Jehovah   ', 'BSCS', 3, 'tu-1005', '1005-y', '$2b$12$JEmigmLE1OQDU4Pbn6.CAeGOcnVhMJ3YeGVMm5f0WKpv8GoXF9g8S');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`idno`),
  ADD UNIQUE KEY `isbn` (`isbn`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `idno` (`idno`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `idno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

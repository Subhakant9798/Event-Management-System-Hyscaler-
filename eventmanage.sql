-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 13, 2024 at 11:18 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `eventmanage`
--

-- --------------------------------------------------------

--
-- Table structure for table `create_event`
--

CREATE TABLE `create_event` (
  `ID` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `datetime` datetime NOT NULL,
  `location` varchar(50) NOT NULL,
  `description` varchar(100) NOT NULL,
  `price` int(11) NOT NULL DEFAULT 1000
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `create_event`
--

INSERT INTO `create_event` (`ID`, `title`, `phone`, `datetime`, `location`, `description`, `price`) VALUES
(34, 'VIGAMA', '7504127861', '2024-05-28 16:47:00', 'E-LEARNING CENTRE', 'a farewell event arranged for our handsome boys and beautiful ladies', 603),
(36, 'ADHRIT', 'BURLA', '2024-05-21 17:50:00', '7978168797', 'A welcome event for creative MCA students!!', 1299),
(37, 'NAMO SHIVAY', 'Bhubaneswar', '2024-05-22 17:41:00', '8260326020', 'Shiv puja with prasad distribution!!', 599);

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL,
  `fed_name` varchar(100) NOT NULL,
  `fed_email` varchar(100) NOT NULL,
  `fed_msg` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`id`, `fed_name`, `fed_email`, `fed_msg`) VALUES
(30, 'zxczxz afcascasc', 'krishnasir34@gmail.com', 'It was great'),
(39, 'Ankit Meher', 'tempankit@gmail.com', 'This event was great!!'),
(40, 'Subhakant Sahoo', 'subhakantsahoo111@gmail.com', 'GREAT EVENT. YOU MADE MY DAY!!');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `id` int(11) NOT NULL,
  `event_name` varchar(50) NOT NULL,
  `no_of_tickets` int(11) NOT NULL,
  `person_name` varchar(50) NOT NULL,
  `amount` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`id`, `event_name`, `no_of_tickets`, `person_name`, `amount`) VALUES
(1, 'Adhrit', 2, 'Subhakant Sahoo', 1600),
(7, 'Car Racing', 2, 'Ankit Meher', 1606),
(12, 'VIGAMA', 3, 'SUBHAM', 1809),
(13, 'ADHRIT', 3, 'Subhakant Sahoo', 3897),
(17, 'VIGAMA', 4, 'Ankit Meher', 2412);

-- --------------------------------------------------------

--
-- Table structure for table `regis_table`
--

CREATE TABLE `regis_table` (
  `ID` int(11) NOT NULL,
  `NAME` varchar(50) NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `PASSWORD` varchar(50) NOT NULL,
  `type` varchar(10) NOT NULL DEFAULT 'user'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `regis_table`
--

INSERT INTO `regis_table` (`ID`, `NAME`, `EMAIL`, `PASSWORD`, `type`) VALUES
(1, 'admin', 'admin', 'admin', 'admin'),
(2, 'snigdha', 'snigdha@gmail.com', 'snigdha', 'user'),
(4, 'subham', 'subhamsahoo789@gmail.com', 'subham', 'user');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `create_event`
--
ALTER TABLE `create_event`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `regis_table`
--
ALTER TABLE `regis_table`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `create_event`
--
ALTER TABLE `create_event`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `regis_table`
--
ALTER TABLE `regis_table`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

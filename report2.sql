-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 04, 2024 at 12:34 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `report2`
--

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

CREATE TABLE `class` (
  `classID` int(11) NOT NULL,
  `year` varchar(30) DEFAULT NULL,
  `term` varchar(30) DEFAULT NULL,
  `class` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`classID`, `year`, `term`, `class`) VALUES
(1001, '2023', '1', 'P.7'),
(1002, '2023', '1', 'P.6'),
(1003, '2023', '1', 'P.5'),
(1004, '2023', '1', 'P.1');

-- --------------------------------------------------------

--
-- Table structure for table `grade`
--

CREATE TABLE `grade` (
  `gradeID` int(11) NOT NULL,
  `class` varchar(50) DEFAULT NULL,
  `mark1` varchar(10) DEFAULT NULL,
  `mark1_1` varchar(10) DEFAULT NULL,
  `grade1` varchar(100) DEFAULT NULL,
  `comment1` varchar(100) DEFAULT NULL,
  `mark2` varchar(10) DEFAULT NULL,
  `mark2_2` varchar(10) DEFAULT NULL,
  `grade2` varchar(100) DEFAULT NULL,
  `comment2` varchar(100) DEFAULT NULL,
  `mark3` varchar(10) DEFAULT NULL,
  `mark3_3` varchar(10) DEFAULT NULL,
  `grade3` varchar(100) DEFAULT NULL,
  `comment3` varchar(100) DEFAULT NULL,
  `mark4` varchar(10) DEFAULT NULL,
  `mark4_4` varchar(10) DEFAULT NULL,
  `grade4` varchar(100) DEFAULT NULL,
  `comment4` varchar(100) DEFAULT NULL,
  `mark5` varchar(10) DEFAULT NULL,
  `mark5_5` varchar(10) DEFAULT NULL,
  `grade5` varchar(100) DEFAULT NULL,
  `comment5` varchar(100) DEFAULT NULL,
  `mark6` varchar(10) DEFAULT NULL,
  `mark6_6` varchar(10) DEFAULT NULL,
  `grade6` varchar(100) DEFAULT NULL,
  `comment6` varchar(100) DEFAULT NULL,
  `mark7` varchar(10) DEFAULT NULL,
  `mark7_7` varchar(10) DEFAULT NULL,
  `grade7` varchar(100) DEFAULT NULL,
  `comment7` varchar(100) DEFAULT NULL,
  `mark8` varchar(10) DEFAULT NULL,
  `mark8_8` varchar(10) DEFAULT NULL,
  `grade8` varchar(100) DEFAULT NULL,
  `comment8` varchar(100) DEFAULT NULL,
  `mark9` varchar(10) DEFAULT NULL,
  `mark9_9` varchar(10) DEFAULT NULL,
  `grade9` varchar(100) DEFAULT NULL,
  `comment9` varchar(100) DEFAULT NULL,
  `mark10` varchar(10) DEFAULT NULL,
  `mark10_10` varchar(10) DEFAULT NULL,
  `grade10` varchar(100) DEFAULT NULL,
  `comment10` varchar(100) DEFAULT NULL,
  `mark11` varchar(10) DEFAULT NULL,
  `mark11_11` varchar(10) DEFAULT NULL,
  `grade11` varchar(100) DEFAULT NULL,
  `comment11` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `grade`
--

INSERT INTO `grade` (`gradeID`, `class`, `mark1`, `mark1_1`, `grade1`, `comment1`, `mark2`, `mark2_2`, `grade2`, `comment2`, `mark3`, `mark3_3`, `grade3`, `comment3`, `mark4`, `mark4_4`, `grade4`, `comment4`, `mark5`, `mark5_5`, `grade5`, `comment5`, `mark6`, `mark6_6`, `grade6`, `comment6`, `mark7`, `mark7_7`, `grade7`, `comment7`, `mark8`, `mark8_8`, `grade8`, `comment8`, `mark9`, `mark9_9`, `grade9`, `comment9`, `mark10`, `mark10_10`, `grade10`, `comment10`, `mark11`, `mark11_11`, `grade11`, `comment11`) VALUES
(1001, 'P.7', '90', '100', 'D.1', 'V.Good', '80', '89', 'D.2', 'Good', '70', '79', 'C.3', 'pass', '60', '69', 'C.4', 'pass', '50', '59', 'C.5', 'pass', '41', '49', 'C.6', 'Fair', '36', '40', 'P.7', 'Tried', '31', '35', 'P.8', 'Fail', '0', '30', 'F.9', 'Fail', '', '', '', '', '', '', '', ''),
(1002, 'P.6', '80', '100', 'D.1', 'V.Good', '75', '79', 'D.2', 'Good', '70', '74', 'C.3', 'pass', '60', '69', 'C.4', 'pass', '50', '59', 'C.5', 'pass', '41', '49', 'C.6', 'Tried', '36', '40', 'P.7', 'Tried', '31', '35', 'P.8', 'Fail', '0', '30', 'F.9', 'Fail', '', '', '', '', '', '', '', ''),
(1003, 'P.5', '90', '100', 'D.1', 'V.Good', '75', '80', 'D.2', 'Good', '70', '74', 'C.3', 'pass', '60', '69', 'C.4', 'pass', '50', '59', 'C.5', 'pass', '41', '49', 'C.6', 'Fair', '36', '40', 'P.7', 'Tried', '11', '35', 'P.8', 'Fail', '0', '10', 'F.9', 'Poor', '', '', '', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `month`
--

CREATE TABLE `month` (
  `testID` int(11) NOT NULL,
  `test` varchar(100) DEFAULT NULL,
  `month` varchar(220) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `month`
--

INSERT INTO `month` (`testID`, `test`, `month`) VALUES
(1001, 'Test1', 'Janary'),
(1002, 'Test2', 'March'),
(1003, 'Test3', 'April');

-- --------------------------------------------------------

--
-- Table structure for table `remarks`
--

CREATE TABLE `remarks` (
  `gradeID` int(11) NOT NULL,
  `class` varchar(70) DEFAULT NULL,
  `fee` varchar(400) DEFAULT NULL,
  `termbegins` varchar(30) DEFAULT NULL,
  `termends` varchar(30) DEFAULT NULL,
  `mark1_1` varchar(30) DEFAULT NULL,
  `mark2_1` varchar(30) DEFAULT NULL,
  `tcomm1` varchar(500) DEFAULT NULL,
  `hcomm1` varchar(500) DEFAULT NULL,
  `mark1_2` varchar(30) DEFAULT NULL,
  `mark2_2` varchar(30) DEFAULT NULL,
  `tcomm2` varchar(500) DEFAULT NULL,
  `hcomm2` varchar(500) DEFAULT NULL,
  `mark1_3` varchar(30) DEFAULT NULL,
  `mark2_3` varchar(30) DEFAULT NULL,
  `tcomm3` varchar(500) DEFAULT NULL,
  `hcomm3` varchar(500) DEFAULT NULL,
  `mark1_4` varchar(30) DEFAULT NULL,
  `mark2_4` varchar(30) DEFAULT NULL,
  `tcomm4` varchar(500) DEFAULT NULL,
  `hcomm4` varchar(500) DEFAULT NULL,
  `mark1_5` varchar(30) DEFAULT NULL,
  `mark2_5` varchar(30) DEFAULT NULL,
  `tcomm5` varchar(500) DEFAULT NULL,
  `hcomm5` varchar(500) DEFAULT NULL,
  `mark1_6` varchar(30) DEFAULT NULL,
  `mark2_6` varchar(30) DEFAULT NULL,
  `tcomm6` varchar(500) DEFAULT NULL,
  `hcomm6` varchar(500) DEFAULT NULL,
  `mark1_7` varchar(30) DEFAULT NULL,
  `mark2_7` varchar(30) DEFAULT NULL,
  `tcomm7` varchar(500) DEFAULT NULL,
  `hcomm7` varchar(500) DEFAULT NULL,
  `mark1_8` varchar(30) DEFAULT NULL,
  `mark2_8` varchar(30) DEFAULT NULL,
  `tcomm8` varchar(500) DEFAULT NULL,
  `hcomm8` varchar(500) DEFAULT NULL,
  `mark1_9` varchar(30) DEFAULT NULL,
  `mark2_9` varchar(30) DEFAULT NULL,
  `tcomm9` varchar(500) DEFAULT NULL,
  `hcomm9` varchar(500) DEFAULT NULL,
  `mark1_10` varchar(30) DEFAULT NULL,
  `mark2_10` varchar(30) DEFAULT NULL,
  `tcomm10` varchar(500) DEFAULT NULL,
  `hcomm10` varchar(500) DEFAULT NULL,
  `requirements` varchar(800) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `remarks`
--

INSERT INTO `remarks` (`gradeID`, `class`, `fee`, `termbegins`, `termends`, `mark1_1`, `mark2_1`, `tcomm1`, `hcomm1`, `mark1_2`, `mark2_2`, `tcomm2`, `hcomm2`, `mark1_3`, `mark2_3`, `tcomm3`, `hcomm3`, `mark1_4`, `mark2_4`, `tcomm4`, `hcomm4`, `mark1_5`, `mark2_5`, `tcomm5`, `hcomm5`, `mark1_6`, `mark2_6`, `tcomm6`, `hcomm6`, `mark1_7`, `mark2_7`, `tcomm7`, `hcomm7`, `mark1_8`, `mark2_8`, `tcomm8`, `hcomm8`, `mark1_9`, `mark2_9`, `tcomm9`, `hcomm9`, `mark1_10`, `mark2_10`, `tcomm10`, `hcomm10`, `requirements`) VALUES
(1001, 'P.7', 'Fees has remained the same as last term', '02/24/2024', '02/25/2024', '4', '12', 'Hardworking Student', '', '13', '24', 'Very Good', '', '25', '28', 'Fair', '', '29', '36', 'fail', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '20 books, 10 heans, 4 pens, 16 boxs, 20 books, 10 heans, 4 pens, 16 boxs, 20 books, 10 heans, 4 pens, 16 boxs, 20 books, 10 heans, 4 pens, 16 boxs'),
(1002, 'P.6', 'Fees has remained the same as last term', '02/24/2024', '02/25/2024', '4', '12', 'Hardworking Student', '', '13', '24', 'Very Good', '', '25', '28', 'Fair', '', '29', '36', 'fail', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '20 books, 10 heans, 4 pens, 16 boxs, 20 books, 10 heans, 4 pens, 16 boxs, 20 books, 10 heans, 4 pens, 16 boxs'),
(1003, 'P.5', 'Fees has remained the same as last term', '02/24/2024', '02/25/2024', '4', '12', 'Hardworking Student', '', '13', '24', 'Very Good', '', '25', '28', 'Fair', '', '29', '36', 'fail', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '20 books, 10 heans, 4 pens, 16 boxs, 20 books, 10 heans, 4 pens, 16 boxs, 20 books, 10 heans, 4 pens, 16 boxs');

-- --------------------------------------------------------

--
-- Table structure for table `result1`
--

CREATE TABLE `result1` (
  `studentID` int(11) NOT NULL,
  `name` varchar(250) DEFAULT NULL,
  `class` varchar(10) DEFAULT NULL,
  `subject` varchar(150) DEFAULT NULL,
  `test1` varchar(20) DEFAULT NULL,
  `test2` varchar(20) DEFAULT NULL,
  `test3` varchar(20) DEFAULT NULL,
  `test4` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `result1`
--

INSERT INTO `result1` (`studentID`, `name`, `class`, `subject`, `test1`, `test2`, `test3`, `test4`) VALUES
(0, '', 'P.6', 'Eng', '', '', '', ''),
(1001, 'lubanjwa Francis', 'P.7', 'Math', '12', '90', '45', '10'),
(1002, 'Mwanje Fred', 'P.7', 'Math', '56', '98', '12', '67'),
(1004, 'Martin Mukisa', 'P.6', 'Eng', '89', '79', '90', '60'),
(1005, 'Sebwato John', 'P.6', 'Eng', '12', '56', '79', '12'),
(1006, 'Sentongo Mathew ', 'P.6', 'Eng', '78', '90', '89', '87'),
(1007, 'Jolly Man', 'P.5', 'Math', '0', '0', '0', '78'),
(1008, 'namu lumansi', 'P.5', 'Math', '0', '0', '0', '90'),
(1009, 'lumu dani', 'P.5', 'Math', '0', '0', '0', '100');

-- --------------------------------------------------------

--
-- Table structure for table `result2`
--

CREATE TABLE `result2` (
  `studentID` int(11) NOT NULL,
  `name` varchar(250) DEFAULT NULL,
  `class` varchar(10) DEFAULT NULL,
  `subject` varchar(150) DEFAULT NULL,
  `test1` varchar(20) DEFAULT NULL,
  `test2` varchar(20) DEFAULT NULL,
  `test3` varchar(20) DEFAULT NULL,
  `test4` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `result2`
--

INSERT INTO `result2` (`studentID`, `name`, `class`, `subject`, `test1`, `test2`, `test3`, `test4`) VALUES
(0, '', 'P.6', 'CRE', '', '', '', ''),
(1004, 'Martin Mukisa', 'P.6', 'CRE', '45', '89', '89', '90'),
(1005, 'Sebwato John', 'P.6', 'CRE', '76', '90', '45', '76'),
(1006, 'Sentongo Mathew ', 'P.6', 'CRE', '87', '76', '98', '76');

-- --------------------------------------------------------

--
-- Table structure for table `result3`
--

CREATE TABLE `result3` (
  `studentID` int(11) NOT NULL,
  `name` varchar(250) DEFAULT NULL,
  `class` varchar(10) DEFAULT NULL,
  `subject` varchar(150) DEFAULT NULL,
  `test1` varchar(20) DEFAULT NULL,
  `test2` varchar(20) DEFAULT NULL,
  `test3` varchar(20) DEFAULT NULL,
  `test4` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `result3`
--

INSERT INTO `result3` (`studentID`, `name`, `class`, `subject`, `test1`, `test2`, `test3`, `test4`) VALUES
(0, '', 'P.5', 'Science', '', '', '', ''),
(1001, 'lubanjwa Francis', 'P.7', 'Eng', '12', '34', '12', '54'),
(1002, 'Mwanje Fred', 'P.7', 'Eng', '98', '65', '78', '23'),
(1004, 'Martin Mukisa', 'P.6', 'Math', '90', '67', '90', '97'),
(1005, 'Sebwato John', 'P.6', 'Math', '78', '98', '54', '89'),
(1006, 'Sentongo Mathew ', 'P.6', 'Math', '45', '76', '56', '89'),
(1007, 'Jolly Man', 'P.5', 'Science', '0', '21', '7', '03'),
(1008, 'namu lumansi', 'P.5', 'Science', '10', '34', '9', '23'),
(1009, 'lumu dani', 'P.5', 'Science', '5', '1', '0', '90');

-- --------------------------------------------------------

--
-- Table structure for table `result4`
--

CREATE TABLE `result4` (
  `studentID` int(11) NOT NULL,
  `name` varchar(250) DEFAULT NULL,
  `class` varchar(10) DEFAULT NULL,
  `subject` varchar(150) DEFAULT NULL,
  `test1` varchar(20) DEFAULT NULL,
  `test2` varchar(20) DEFAULT NULL,
  `test3` varchar(20) DEFAULT NULL,
  `test4` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `result5`
--

CREATE TABLE `result5` (
  `studentID` int(11) NOT NULL,
  `name` varchar(250) DEFAULT NULL,
  `class` varchar(10) DEFAULT NULL,
  `subject` varchar(150) DEFAULT NULL,
  `test1` varchar(20) DEFAULT NULL,
  `test2` varchar(20) DEFAULT NULL,
  `test3` varchar(20) DEFAULT NULL,
  `test4` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `result5`
--

INSERT INTO `result5` (`studentID`, `name`, `class`, `subject`, `test1`, `test2`, `test3`, `test4`) VALUES
(0, '', 'P.6', 'Science', '', '', '', ''),
(1001, 'lubanjwa Francis', 'P.7', 'Science', '12', '45', '0', '58'),
(1002, 'Mwanje Fred', 'P.7', 'Science', '32', '12', '2', '67'),
(1004, 'Martin Mukis', 'P.6', 'Science', '90', '65', '78', '100'),
(1005, 'Sebwato John', 'P.6', 'Science', '67', '89', '78', '65'),
(1006, 'Sentongo Mathew ', 'P.6', 'Science', '78', '87', '89', '79'),
(1007, 'Jolly Man', 'P.5', 'English', '78', '45', '87', '79'),
(1008, 'namu lumansi', 'P.5', 'English', '23', '76', '74', '32'),
(1009, 'lumu dani', 'P.5', 'English', '87', '74', '32', '16');

-- --------------------------------------------------------

--
-- Table structure for table `result6`
--

CREATE TABLE `result6` (
  `studentID` int(11) NOT NULL,
  `name` varchar(250) DEFAULT NULL,
  `class` varchar(10) DEFAULT NULL,
  `subject` varchar(150) DEFAULT NULL,
  `test1` varchar(20) DEFAULT NULL,
  `test2` varchar(20) DEFAULT NULL,
  `test3` varchar(20) DEFAULT NULL,
  `test4` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `result7`
--

CREATE TABLE `result7` (
  `studentID` int(11) NOT NULL,
  `name` varchar(250) DEFAULT NULL,
  `class` varchar(10) DEFAULT NULL,
  `subject` varchar(150) DEFAULT NULL,
  `test1` varchar(20) DEFAULT NULL,
  `test2` varchar(20) DEFAULT NULL,
  `test3` varchar(20) DEFAULT NULL,
  `test4` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `result7`
--

INSERT INTO `result7` (`studentID`, `name`, `class`, `subject`, `test1`, `test2`, `test3`, `test4`) VALUES
(0, '', 'P.5', 'SST', '', '', '', ''),
(1001, 'lubanjwa Francis', 'P.7', 'SST', '0', '0', '0', '60'),
(1002, 'Mwanje Fred', 'P.7', 'SST', '67', '12', '0', '54'),
(1004, 'Martin Mukisa', 'P.6', 'SST', '90', '67', '89', '99'),
(1005, 'Sebwato John', 'P.6', 'SST', '34', '67', '87', '45'),
(1006, 'Sentongo Mathew ', 'P.6', 'SST', '78', '89', '67', '98'),
(1007, 'Jolly Man', 'P.5', 'SST', '23', '54', '78', '90'),
(1008, 'namu lumansi', 'P.5', 'SST', '75', '98', '73', '97'),
(1009, 'lumu dani', 'P.5', 'SST', '43', '98', '78', '12');

-- --------------------------------------------------------

--
-- Table structure for table `result8`
--

CREATE TABLE `result8` (
  `studentID` int(11) NOT NULL,
  `name` varchar(250) DEFAULT NULL,
  `class` varchar(10) DEFAULT NULL,
  `subject` varchar(150) DEFAULT NULL,
  `test1` varchar(20) DEFAULT NULL,
  `test2` varchar(20) DEFAULT NULL,
  `test3` varchar(20) DEFAULT NULL,
  `test4` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `ref` int(11) NOT NULL,
  `name` varchar(250) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `class` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `age` varchar(20) DEFAULT NULL,
  `nationality` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `image` varchar(400) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`ref`, `name`, `gender`, `status`, `class`, `dob`, `age`, `nationality`, `address`, `image`) VALUES
(1001, 'lubanjwa Francis', 'Male', 'Day', 'P.7', '05/02/2024', '16', 'Ugandan', 'Kabimbiri', 'E:/mast/Snapchat-1002590576.jpg'),
(1002, 'Mwanje Fred', 'Male', 'Day', 'P.7', '2/3/2002', '19', 'Ugandan', 'Kayunga', 'D:/MEDIA/PHOTES/IMG_20210212_141320.jpg'),
(1003, 'Maama Alpha', 'Female', 'Day', 'P.7', '', '26', 'Select', '', 'D:/MEDIA/PHOTES/CollageMaker_20229475953276.jpg'),
(1004, 'Martin Mukisa', 'Male', 'Day', 'P.6', '', '', 'Select', '', 'D:/MEDIA/PHOTES/MY PHOTOS/Sent/IMG-20220124-WA0063.jpg'),
(1005, 'Sebwato John', 'Male', 'Day', 'P.6', '', '', 'Select', '', 'D:/MEDIA/PHOTES/MY PHOTOS/Sent/IMG-20211204-WA0031.jpg'),
(1006, 'Sentongo Mathew ', 'Male', 'Day', 'P.6', '', '', 'Select', '', 'D:/MEDIA/PHOTES/MY PHOTOS/Sent/IMG-20220114-WA0040.jpg'),
(1007, 'Jolly Man', 'Male', 'Day', 'P.5', '', '', 'Select', '', 'D:/MEDIA/PHOTES/PHOTOS/00cb028473b84c8aae44a1552cf508df(2).jpg'),
(1008, 'namu lumansi', 'Female', 'Border', 'P.5', '', '', 'Select', '', 'D:/MEDIA/PHOTES/PHOTOS/1b5e56f73d7c4dd18c8f79a2e15b188f.jpg'),
(1009, 'lumu dani', 'Female', 'Border', 'P.5', '', '', 'Select', '', 'D:/MEDIA/PHOTES/PHOTOS/2b1bb485fba543a6b5c95f1fbc651e08.jpg'),
(1010, 'KALEMA', 'Male', 'Day', 'P.6', '2024-04-10', '', 'Ugandan', 'GGG', '');

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `subjectID` int(11) NOT NULL,
  `class` varchar(100) DEFAULT NULL,
  `classteacher` varchar(220) DEFAULT NULL,
  `subject1` varchar(200) DEFAULT NULL,
  `teacher1` varchar(200) DEFAULT NULL,
  `subject2` varchar(200) DEFAULT NULL,
  `teacher2` varchar(200) DEFAULT NULL,
  `subject3` varchar(200) DEFAULT NULL,
  `teacher3` varchar(100) DEFAULT NULL,
  `subject4` varchar(200) DEFAULT NULL,
  `teacher4` varchar(100) DEFAULT NULL,
  `subject5` varchar(200) DEFAULT NULL,
  `teacher5` varchar(100) DEFAULT NULL,
  `subject6` varchar(200) DEFAULT NULL,
  `teacher6` varchar(100) DEFAULT NULL,
  `subject7` varchar(200) DEFAULT NULL,
  `teacher7` varchar(100) DEFAULT NULL,
  `subject8` varchar(200) DEFAULT NULL,
  `teacher8` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`subjectID`, `class`, `classteacher`, `subject1`, `teacher1`, `subject2`, `teacher2`, `subject3`, `teacher3`, `subject4`, `teacher4`, `subject5`, `teacher5`, `subject6`, `teacher6`, `subject7`, `teacher7`, `subject8`, `teacher8`) VALUES
(1001, 'P.7', 'Emma', 'Math', 'Twesige Emma', '', 'Select', 'Eng', 'Nakintu Ruth', '', 'Select', 'Science', 'Moses Katende', '', 'Select', 'SST', 'Francis Lubanjwa', '', 'Select'),
(1002, 'P.6', 'Francis Lubanjwa', 'Eng', 'Lubanjwa John', 'CRE', 'Francis Lubanjwa', 'Math', 'Francis Lubanjwa', '', 'Select', 'Science', 'Twesige Emma', '', 'Select', 'SST', 'Twesige Emma', '', 'Select'),
(1003, 'P.5', 'Emma', 'Math', 'Lubanjwa John', '', 'Select', 'Science', 'Francis Lubanjwa', '', 'Select', 'English', 'Nakintu Ruth', '', 'Select', 'SST', 'Moses Katende', '', 'Select');

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `ref` int(11) NOT NULL,
  `name` varchar(250) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `nationality` varchar(100) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`ref`, `name`, `gender`, `mobile`, `email`, `nationality`, `address`) VALUES
(1002, 'Nakintu Ruth', 'Male', '786454678', 'ruth', 'Ugandan', 'Kampala'),
(1003, 'me', 'Male', '09876', 'male@123', 'Ugandan', 'Bugema');

-- --------------------------------------------------------

--
-- Table structure for table `term`
--

CREATE TABLE `term` (
  `termID` int(11) NOT NULL,
  `year` varchar(20) DEFAULT NULL,
  `term` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `term`
--

INSERT INTO `term` (`termID`, `year`, `term`) VALUES
(1001, '2023', '1');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `ref` int(11) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `role` varchar(100) DEFAULT NULL,
  `password1` varchar(70) DEFAULT NULL,
  `password2` varchar(70) DEFAULT NULL,
  `image` varchar(400) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`ref`, `username`, `email`, `role`, `password1`, `password2`, `image`) VALUES
(1001, 'francis', 'francis@gmail.com', 'Teacher', '111', '111', ''),
(1003, 'luba', 'luba@gmail.com', 'DOS', '111', '111', 'D:/MEDIA/PHOTES/CollageMaker_202291110619235.jpg'),
(1004, 'francis', 'francis@123', 'Teacher', '222', '222', ''),
(1005, 'francis', 'francis@123', 'Secretory', '222', '222', ''),
(1006, 'francis', 'francis@123', 'Secretory', '222', '222', '');

-- --------------------------------------------------------

--
-- Table structure for table `year`
--

CREATE TABLE `year` (
  `yearID` int(11) NOT NULL,
  `year` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `year`
--

INSERT INTO `year` (`yearID`, `year`) VALUES
(1001, '2023');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`classID`);

--
-- Indexes for table `grade`
--
ALTER TABLE `grade`
  ADD PRIMARY KEY (`gradeID`);

--
-- Indexes for table `month`
--
ALTER TABLE `month`
  ADD PRIMARY KEY (`testID`);

--
-- Indexes for table `remarks`
--
ALTER TABLE `remarks`
  ADD PRIMARY KEY (`gradeID`);

--
-- Indexes for table `result1`
--
ALTER TABLE `result1`
  ADD PRIMARY KEY (`studentID`);

--
-- Indexes for table `result2`
--
ALTER TABLE `result2`
  ADD PRIMARY KEY (`studentID`);

--
-- Indexes for table `result3`
--
ALTER TABLE `result3`
  ADD PRIMARY KEY (`studentID`);

--
-- Indexes for table `result4`
--
ALTER TABLE `result4`
  ADD PRIMARY KEY (`studentID`);

--
-- Indexes for table `result5`
--
ALTER TABLE `result5`
  ADD PRIMARY KEY (`studentID`);

--
-- Indexes for table `result6`
--
ALTER TABLE `result6`
  ADD PRIMARY KEY (`studentID`);

--
-- Indexes for table `result7`
--
ALTER TABLE `result7`
  ADD PRIMARY KEY (`studentID`);

--
-- Indexes for table `result8`
--
ALTER TABLE `result8`
  ADD PRIMARY KEY (`studentID`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`ref`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`subjectID`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`ref`);

--
-- Indexes for table `term`
--
ALTER TABLE `term`
  ADD PRIMARY KEY (`termID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`ref`);

--
-- Indexes for table `year`
--
ALTER TABLE `year`
  ADD PRIMARY KEY (`yearID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

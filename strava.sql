-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: localhost    Database: strava
-- ------------------------------------------------------
-- Server version	8.0.27-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Buelta`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE IF NOT EXISTS `Buelta` (
  `ID` varchar(20) NOT NULL,
  `denbora` int DEFAULT NULL,
  `IDEntrena` varchar(20) DEFAULT NULL,
  `izena` varchar(20) DEFAULT NULL,
  `distantzia` float DEFAULT NULL,
  PRIMARY KEY (`ID`),
  /*KEY `IDEntrena` (`IDEntrena`),*/
  CONSTRAINT `Buelta_ibfk_1` FOREIGN KEY (`IDEntrena`) REFERENCES `Entrenamendua` (`ID`)
)
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Buelta`
--

--
-- Table structure for table `Ekipamendua`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE IF NOT EXISTS `Ekipamendua` (
  `ID` varchar(20) NOT NULL,
  `marka` varchar(20) DEFAULT NULL,
  `modelo` varchar(20) DEFAULT NULL,
  `izena` varchar(20) DEFAULT NULL,
  `distantzia` float DEFAULT NULL,
  PRIMARY KEY (`ID`)
) 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ekipamendua`
--

--
-- Table structure for table `Entrenamendua`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE IF NOT EXISTS `Entrenamendua` (
  `ID` varchar(20) NOT NULL,
  `mota` varchar(20) DEFAULT NULL,
  `denbora` int DEFAULT NULL,
  `izena` varchar(20) DEFAULT NULL,
  `hasieraData` varchar(20) DEFAULT NULL,
  `distantzia` float DEFAULT NULL,
  `ikusgarritasuna` varchar(20) DEFAULT NULL,
  `abiaduraBzb` float DEFAULT NULL,
  `abiaduraMax` float DEFAULT NULL,
  PRIMARY KEY (`ID`)
) 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Entrenamendua`
--
--
-- Table structure for table `Jarraitzaile`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE IF NOT EXISTS `Jarraitzaile` (
  `izena` varchar(20) NOT NULL,
  `abizena` varchar(20) NOT NULL,
  PRIMARY KEY (`izena`,`abizena`)
) 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Jarraitzaile`
--
--
-- Table structure for table `Komentario`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE IF NOT EXISTS `Komentario` (
  `komentarioIgorleIzena` varchar(20) DEFAULT NULL,
  `komentarioIgorleAbizena` varchar(20) DEFAULT NULL,
  `komentarioTestua` varchar(200) DEFAULT NULL,
  `komentarioId` int NOT NULL,
  `komentarioData` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`komentarioId`),
  /*KEY `komentarioIgorleIzena` (`komentarioIgorleIzena`,`komentarioIgorleAbizena`),*/
  CONSTRAINT `Komentario_ibfk_1` FOREIGN KEY (`komentarioIgorleIzena`, `komentarioIgorleAbizena`) REFERENCES `Jarraitzaile` (`izena`, `abizena`)
)
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Komentario`
--
--
-- Table structure for table `Medizioak`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE IF NOT EXISTS`Medizioak` (
  `dataOrdua` datetime NOT NULL,
  `IDBuelta` varchar(20) DEFAULT NULL,
  `pultsazioBzb` float DEFAULT NULL,
  `pultsazioMax` float DEFAULT NULL,
  `abiaduraBzb` float DEFAULT NULL,
  `abiaduraMax` float DEFAULT NULL,
  PRIMARY KEY (`dataOrdua`),
  /*KEY `IDBuelta` (`IDBuelta`),*/
  CONSTRAINT `Medizioak_ibfk_1` FOREIGN KEY (`IDBuelta`) REFERENCES `Buelta` (`ID`)
)
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medizioak`
--
--
-- Table structure for table `Segmentua`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE IF NOT EXISTS `Segmentua` (
  `ID` varchar(20) NOT NULL,
  `denbora` int DEFAULT NULL,
  `izena` varchar(20) DEFAULT NULL,
  `distantzia` float DEFAULT NULL,
  `hasieraData` varchar(20) DEFAULT NULL,
  `IDEntrenamendua` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  /*KEY `IDEntrenamendua` (`IDEntrenamendua`),*/
  CONSTRAINT `Segmentua_ibfk_1` FOREIGN KEY (`IDEntrenamendua`) REFERENCES `Entrenamendua` (`ID`)
)
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Segmentua`
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-29 12:48:52
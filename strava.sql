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

DROP TABLE IF EXISTS `Buelta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Buelta` (
  `ID` int NOT NULL,
  `denbora` int DEFAULT NULL,
  `IDEntrena` int DEFAULT NULL,
  `izena` varchar(20) DEFAULT NULL,
  `distantzia` float DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `IDEntrena` (`IDEntrena`),
  CONSTRAINT `Buelta_ibfk_1` FOREIGN KEY (`IDEntrena`) REFERENCES `Entrenamendua` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Buelta`
--

LOCK TABLES `Buelta` WRITE;
/*!40000 ALTER TABLE `Buelta` DISABLE KEYS */;
/*!40000 ALTER TABLE `Buelta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ekipamendua`
--

DROP TABLE IF EXISTS `Ekipamendua`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ekipamendua` (
  `ID` int NOT NULL,
  `marka` varchar(20) DEFAULT NULL,
  `modelo` varchar(20) DEFAULT NULL,
  `izena` varchar(20) DEFAULT NULL,
  `distantzia` float DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ekipamendua`
--

LOCK TABLES `Ekipamendua` WRITE;
/*!40000 ALTER TABLE `Ekipamendua` DISABLE KEYS */;
/*!40000 ALTER TABLE `Ekipamendua` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Entrenamendua`
--

DROP TABLE IF EXISTS `Entrenamendua`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Entrenamendua` (
  `ID` int NOT NULL,
  `mota` varchar(20) DEFAULT NULL,
  `denbora` int DEFAULT NULL,
  `izena` varchar(20) DEFAULT NULL,
  `hasieraData` varchar(20) DEFAULT NULL,
  `distantzia` float DEFAULT NULL,
  `ikusgarritasuna` varchar(20) DEFAULT NULL,
  `abiaduraBzb` float DEFAULT NULL,
  `abiaduraMax` float DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Entrenamendua`
--

LOCK TABLES `Entrenamendua` WRITE;
/*!40000 ALTER TABLE `Entrenamendua` DISABLE KEYS */;
/*!40000 ALTER TABLE `Entrenamendua` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Jarraitzaile`
--

DROP TABLE IF EXISTS `Jarraitzaile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Jarraitzaile` (
  `izena` varchar(20) NOT NULL,
  `abizena` varchar(20) NOT NULL,
  PRIMARY KEY (`izena`,`abizena`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Jarraitzaile`
--

LOCK TABLES `Jarraitzaile` WRITE;
/*!40000 ALTER TABLE `Jarraitzaile` DISABLE KEYS */;
/*!40000 ALTER TABLE `Jarraitzaile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Komentario`
--

DROP TABLE IF EXISTS `Komentario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Komentario` (
  `komentarioIgorleIzena` varchar(20) DEFAULT NULL,
  `komentarioIgorleAbizena` varchar(20) DEFAULT NULL,
  `komentarioTestua` varchar(200) DEFAULT NULL,
  `komentarioId` int NOT NULL,
  `komentarioData` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`komentarioId`),
  KEY `komentarioIgorleIzena` (`komentarioIgorleIzena`,`komentarioIgorleAbizena`),
  CONSTRAINT `Komentario_ibfk_1` FOREIGN KEY (`komentarioIgorleIzena`, `komentarioIgorleAbizena`) REFERENCES `Jarraitzaile` (`izena`, `abizena`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Komentario`
--

LOCK TABLES `Komentario` WRITE;
/*!40000 ALTER TABLE `Komentario` DISABLE KEYS */;
/*!40000 ALTER TABLE `Komentario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Medizioak`
--

DROP TABLE IF EXISTS `Medizioak`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Medizioak` (
  `dataOrdua` datetime NOT NULL,
  `IDBuelta` int DEFAULT NULL,
  `pultsazioBzb` float DEFAULT NULL,
  `pultsazioMax` float DEFAULT NULL,
  `abiaduraBzb` float DEFAULT NULL,
  `abiaduraMax` float DEFAULT NULL,
  PRIMARY KEY (`dataOrdua`),
  KEY `IDBuelta` (`IDBuelta`),
  CONSTRAINT `Medizioak_ibfk_1` FOREIGN KEY (`IDBuelta`) REFERENCES `Buelta` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medizioak`
--

LOCK TABLES `Medizioak` WRITE;
/*!40000 ALTER TABLE `Medizioak` DISABLE KEYS */;
/*!40000 ALTER TABLE `Medizioak` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Segmentua`
--

DROP TABLE IF EXISTS `Segmentua`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Segmentua` (
  `ID` int NOT NULL,
  `denbora` int DEFAULT NULL,
  `izena` varchar(20) DEFAULT NULL,
  `distantzia` float DEFAULT NULL,
  `hasieraData` varchar(20) DEFAULT NULL,
  `IDEntrenamendua` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_IDEntrenamendua` (`IDEntrenamendua`),
  CONSTRAINT `fk_IDEntrenamendua` FOREIGN KEY (`IDEntrenamendua`) REFERENCES `Entrenamendua` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Segmentua`
--

LOCK TABLES `Segmentua` WRITE;
/*!40000 ALTER TABLE `Segmentua` DISABLE KEYS */;
/*!40000 ALTER TABLE `Segmentua` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-24 12:57:45

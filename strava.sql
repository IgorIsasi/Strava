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
  `km` int DEFAULT NULL,
  `denbora` int DEFAULT NULL,
  `IDEntrena` int DEFAULT NULL,
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
  `deskribapena` varchar(100) DEFAULT NULL,
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
  `noizHasi` datetime DEFAULT NULL,
  `mota` varchar(20) DEFAULT NULL,
  `denbora` int DEFAULT NULL,
  `km` int DEFAULT NULL,
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
-- Table structure for table `Erabili`
--

DROP TABLE IF EXISTS `Erabili`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Erabili` (
  `IDEkipamendu` int NOT NULL,
  `IDEntrena` int NOT NULL,
  PRIMARY KEY (`IDEkipamendu`,`IDEntrena`),
  KEY `IDEntrena` (`IDEntrena`),
  CONSTRAINT `Erabili_ibfk_1` FOREIGN KEY (`IDEkipamendu`) REFERENCES `Ekipamendua` (`ID`),
  CONSTRAINT `Erabili_ibfk_2` FOREIGN KEY (`IDEntrena`) REFERENCES `Entrenamendua` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Erabili`
--

LOCK TABLES `Erabili` WRITE;
/*!40000 ALTER TABLE `Erabili` DISABLE KEYS */;
/*!40000 ALTER TABLE `Erabili` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Gustatu`
--

DROP TABLE IF EXISTS `Gustatu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Gustatu` (
  `IDEntrena` int NOT NULL,
  `jIzenAbizenak` varchar(30) NOT NULL,
  PRIMARY KEY (`IDEntrena`,`jIzenAbizenak`),
  KEY `jIzenAbizenak` (`jIzenAbizenak`),
  CONSTRAINT `Gustatu_ibfk_1` FOREIGN KEY (`IDEntrena`) REFERENCES `Entrenamendua` (`ID`),
  CONSTRAINT `Gustatu_ibfk_2` FOREIGN KEY (`jIzenAbizenak`) REFERENCES `Jarraitzaile` (`izenAbizenak`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Gustatu`
--

LOCK TABLES `Gustatu` WRITE;
/*!40000 ALTER TABLE `Gustatu` DISABLE KEYS */;
/*!40000 ALTER TABLE `Gustatu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Jarraitzaile`
--

DROP TABLE IF EXISTS `Jarraitzaile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Jarraitzaile` (
  `izenAbizenak` varchar(30) NOT NULL,
  PRIMARY KEY (`izenAbizenak`)
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
-- Table structure for table `Komentatu`
--

DROP TABLE IF EXISTS `Komentatu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Komentatu` (
  `IDEntrena` int NOT NULL,
  `jIzenAbizenak` varchar(30) NOT NULL,
  `testua` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`IDEntrena`,`jIzenAbizenak`),
  KEY `jIzenAbizenak` (`jIzenAbizenak`),
  CONSTRAINT `Komentatu_ibfk_1` FOREIGN KEY (`IDEntrena`) REFERENCES `Entrenamendua` (`ID`),
  CONSTRAINT `Komentatu_ibfk_2` FOREIGN KEY (`jIzenAbizenak`) REFERENCES `Jarraitzaile` (`izenAbizenak`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Komentatu`
--

LOCK TABLES `Komentatu` WRITE;
/*!40000 ALTER TABLE `Komentatu` DISABLE KEYS */;
/*!40000 ALTER TABLE `Komentatu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Medizioak`
--

DROP TABLE IF EXISTS `Medizioak`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Medizioak` (
  `dataOrdua` datetime NOT NULL,
  `posizioaLat` float DEFAULT NULL,
  `posizioaLong` float DEFAULT NULL,
  `pultsazioak` float DEFAULT NULL,
  `abiadura` float DEFAULT NULL,
  `IDBuelta` int DEFAULT NULL,
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
-- Table structure for table `Segmentatu`
--

DROP TABLE IF EXISTS `Segmentatu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Segmentatu` (
  `IDSegmentu` int NOT NULL,
  `IDEntrena` int NOT NULL,
  PRIMARY KEY (`IDSegmentu`,`IDEntrena`),
  KEY `IDEntrena` (`IDEntrena`),
  CONSTRAINT `Segmentatu_ibfk_1` FOREIGN KEY (`IDSegmentu`) REFERENCES `Segmentua` (`ID`),
  CONSTRAINT `Segmentatu_ibfk_2` FOREIGN KEY (`IDEntrena`) REFERENCES `Entrenamendua` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Segmentatu`
--

LOCK TABLES `Segmentatu` WRITE;
/*!40000 ALTER TABLE `Segmentatu` DISABLE KEYS */;
/*!40000 ALTER TABLE `Segmentatu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Segmentua`
--

DROP TABLE IF EXISTS `Segmentua`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Segmentua` (
  `ID` int NOT NULL,
  `hasieraPosLat` float DEFAULT NULL,
  `hasierakoPosLong` float DEFAULT NULL,
  `bukaerakoPosLat` float DEFAULT NULL,
  `bukaerakoPosLong` float DEFAULT NULL,
  `denbora` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
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

-- Dump completed on 2021-11-22 10:35:36

-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: bike17
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `map_usertravel`
--

DROP TABLE IF EXISTS `map_usertravel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `map_usertravel` (
  `MAP_USERID` varchar(20) NOT NULL,
  `MAP_LISTID` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `map_usertravel`
--

LOCK TABLES `map_usertravel` WRITE;
/*!40000 ALTER TABLE `map_usertravel` DISABLE KEYS */;
INSERT INTO `map_usertravel` VALUES ('lindali@aliyun.com','2019-11-02 17:07:54'),('lindali@aliyun.com','2019-11-02 17:26:50'),('lindali@aliyun.com','2019-11-02 17:41:54'),('lindali@aliyun.com','2019-11-02 18:04:05'),('lindali@aliyun.com','2019-11-02 18:46:08'),('lindali@aliyun.com','2019-11-02 18:46:53'),('lindali@aliyun.com','2019-11-02 21:30:20'),('lindali@aliyun.com','2019-11-02 21:31:09'),('lindali@aliyun.com','2019-11-02 21:31:48'),('lindali@aliyun.com','2019-11-02 21:32:37'),('lindali@aliyun.com','2019-11-02 21:33:53'),('lindali@aliyun.com','2019-11-02 22:00:38'),('lindali@aliyun.com','2019-11-02 22:01:45'),('lindali@aliyun.com','2019-11-02 22:05:24'),('lindali@aliyun.com','2019-11-02 22:05:41'),('lindali@aliyun.com','2019-11-02 22:07:46'),('lindali@aliyun.com','2019-11-02 22:10:01'),('lindali@aliyun.com','Travel_plan1110.4011967586364567'),('lindali@aliyun.com','Travel0.5603202521431448'),('lindali@aliyun.com','Travel_plan1110.36264546808101744'),('lindali@aliyun.com','Travel0.31182077090425486'),('lindali@aliyun.com','Travel_plan1110.7262466668395761'),('lindali@aliyun.com','Travel_plan1110.03704315241150852'),('lindali@aliyun.com','Travel0.6110713152317995'),('lindali@aliyun.com','Travel_plan1110.5468886825692735'),('lindali@aliyun.com','Travel_plan1110.9305797097557966'),('lindali@aliyun.com','Travel_plan1110.49754475289727074'),('lindali@aliyun.com','Travel0.19685044344221284'),('lindali@aliyun.com','Travel_plan1110.9924840833921769'),('lindali@aliyun.com','Travel_plan0.424864970543296'),('JAMES@GMAIL.COM','Travel_plan1110.5657841521927939'),('lindali@aliyun.com','Travel_plan0.5973842242708283'),('lindali@aliyun.com','Travel_plan110.4703210084422687'),('lindali@aliyun.com','Travel_plan120.14075514594163294'),('lily@gmail.com','Travel_plan0.24365696892482877'),('lily@gmail.com','Travel_plan0.4730749702761648'),('lily@gmail.com','Travel_plan0.1352694771581045'),('lily@gmail.com','Travel_plan0.7579880214836336'),('lily@gmail.com','Travel_plan0.8849971842812348'),('lily@gmail.com','Travel_plan0.6518873643613303'),('lily@gmail.com','Travel_plan0.10531078661355263');
/*!40000 ALTER TABLE `map_usertravel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `travellist`
--

DROP TABLE IF EXISTS `travellist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `travellist` (
  `LIST_ID` varchar(255) NOT NULL,
  `LIST_CRATETIME` varchar(25) DEFAULT NULL,
  `LIST_USERID` varchar(25) DEFAULT NULL,
  `LIST_DEPARTURE` varchar(25) DEFAULT NULL,
  `LIST_DESTINATION` varchar(225) DEFAULT NULL,
  `LIST_PLANTIME` varchar(45) DEFAULT NULL,
  `LIST_TRAVELTITLE` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`LIST_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `travellist`
--

LOCK TABLES `travellist` WRITE;
/*!40000 ALTER TABLE `travellist` DISABLE KEYS */;
INSERT INTO `travellist` VALUES ('Travel_plan0.10531078661355263','2019-11-03 15:27:01','lily@gmail.com','BARROW_STREET','CHATHAM_STREET','2019-11-05T21:10','Travel_plan'),('Travel_plan0.1352694771581045','2019-11-03 15:18:29','lily@gmail.com','BARROW_STREET','CHRISTCHURCH_PLACE','2019-11-05T09:10','Travel_plan'),('Travel_plan0.24365696892482877','2019-11-03 14:49:45','lily@gmail.com','BOLTON_STREET','CITY_QUAY','2019-11-05T09:01','Travel_plan'),('Travel_plan0.4730749702761648','2019-11-03 14:59:51','lily@gmail.com','BARROW_STREET','CHRISTCHURCH_PLACE','2019-11-05T21:10','Travel_plan'),('Travel_plan0.6518873643613303','2019-11-03 15:23:42','lily@gmail.com','BARROW_STREET','BENSON_STREET','2019-11-05T21:10','Travel_plan'),('Travel_plan0.7579880214836336','2019-11-03 15:20:19','lily@gmail.com','BENSON_STREET','CHRISTCHURCH_PLACE','2019-11-05T21:10','Travel_plan'),('Travel_plan0.8849971842812348','2019-11-03 15:23:02','lily@gmail.com','BARROW_STREET','CATHAL_BRUGHA_STREET','2019-11-05T10:59','Travel_plan'),('Travel_plan1110.5657841521927939','2019-11-02 22:50:31','JAMES@GMAIL.COM','BENSON_STREET','CHRISTCHURCH_PLACE','2019-11-05T09:10','Travel_plan111');
/*!40000 ALTER TABLE `travellist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `USER_ID` varchar(20) NOT NULL,
  `USER_NAME` varchar(25) DEFAULT NULL,
  `REGRIST_DATE` datetime DEFAULT NULL,
  `ROLE_TYPE` varchar(25) DEFAULT NULL,
  `EMAIL` varchar(225) DEFAULT NULL,
  `password` varchar(225) DEFAULT NULL,
  PRIMARY KEY (`USER_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('JAMES@GMAIL.COM','JAMES','2019-11-02 22:49:51','user','JAMES@GMAIL.COM','james'),('lily@gmail.com','lily','2019-11-02 23:16:20','user','lily@gmail.com','lily'),('lindali@aliyun.com','lindali','2019-10-13 22:27:37','user','lindali@aliyun.com','lindali');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-03 15:49:19

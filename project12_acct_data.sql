
-- Host: localhost    Database: project12
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `acct_data`
--
DROP Database IF EXISTS `project12`;
CREATE Database `project12`;
use project12;
DROP TABLE IF EXISTS `acct_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `acct_data` (
  `name` varchar(20) DEFAULT NULL,
  `mobile_num` varchar(10) DEFAULT NULL,
  `dob` varchar(12) DEFAULT NULL,
  `pin` int NOT NULL,
  `account_no` int NOT NULL,
  `gender` char(1) DEFAULT NULL,
  `balance` int DEFAULT '50',
  PRIMARY KEY (`account_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acct_data`
--

*LOCK TABLES `acct_data` WRITE;
/*!40000 ALTER TABLE `acct_data` DISABLE KEYS */;
INSERT INTO `acct_data` VALUES ('Dummy_User','1234696969','14/02/2023',12345,25268686,'O',5000);
/*!40000 ALTER TABLE `acct_data` ENABLE KEYS */;
UNLOCK TABLES;
CREATE TABLE `u25268686` (
  `date` varchar(12) DEFAULT NULL,
  `person2` varchar(20) DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `who` char(1) DEFAULT NULL,
  `newbal` int DEFAULT NULL,
  `c_d` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;


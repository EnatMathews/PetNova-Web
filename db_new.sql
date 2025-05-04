/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - pet_care
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`pet_care` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `pet_care`;

/*Table structure for table `appointment` */

DROP TABLE IF EXISTS `appointment`;

CREATE TABLE `appointment` (
  `appointment_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `appointment_date` varchar(100) DEFAULT NULL,
  `appointment_time` varchar(100) DEFAULT NULL,
  `appointment_status` varchar(100) DEFAULT NULL,
  `doctor_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`appointment_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `appointment` */

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `sender_type` varchar(100) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `receiver_type` varchar(100) DEFAULT NULL,
  `chat_message` varchar(100) DEFAULT NULL,
  `chat_date` varchar(100) DEFAULT NULL,
  `chat_time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`sender_id`,`sender_type`,`receiver_id`,`receiver_type`,`chat_message`,`chat_date`,`chat_time`) values 
(1,1,'doctor',5,'user','hloo','2024-12-25','20:38:18'),
(2,1,'doctor',5,'user','hy','2024-12-25','21:04:48'),
(3,5,'user',1,'pet_sitting','loo','2025-02-14','10:15:54'),
(4,1,'pet_sitting',5,'user','hy','2025-02-14','10:45:45'),
(5,1,'pet_sitting',5,'user','hy','2025-02-14','10:47:53'),
(6,1,'pet_sitting',5,'user','loo','2025-02-14','10:47:59'),
(7,5,'user',1,'pet_sitting','good morning','2025-02-14','11:11:59'),
(8,5,'user',1,'pet_sitting','i would like to know about services','2025-02-14','11:12:15'),
(9,1,'pet_sitting',5,'user','okie','2025-02-14','11:13:15');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `complaint` varchar(1000) DEFAULT NULL,
  `complaint_reply` varchar(1000) DEFAULT NULL,
  `complaint_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`login_id`,`complaint`,`complaint_reply`,`complaint_date`) values 
(1,6,'hy','pending','2025-02-14');

/*Table structure for table `doctor` */

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `doctor_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `doctor_fname` varchar(100) DEFAULT NULL,
  `doctor_lname` varchar(100) DEFAULT NULL,
  `doctor_email` varchar(100) DEFAULT NULL,
  `doctor_phone` varchar(100) DEFAULT NULL,
  `doctor_place` varchar(100) DEFAULT NULL,
  `doctor_qualification` varchar(100) DEFAULT NULL,
  `doctor_experience` varchar(100) DEFAULT NULL,
  `doctor_certificate` varchar(10000) DEFAULT NULL,
  PRIMARY KEY (`doctor_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `doctor` */

insert  into `doctor`(`doctor_id`,`login_id`,`doctor_fname`,`doctor_lname`,`doctor_email`,`doctor_phone`,`doctor_place`,`doctor_qualification`,`doctor_experience`,`doctor_certificate`) values 
(1,1,'Ronald','Jose','Rono@gmail.com','7896541235','Thrissur','mbbs,md','4',NULL);

/*Table structure for table `doctor_payment` */

DROP TABLE IF EXISTS `doctor_payment`;

CREATE TABLE `doctor_payment` (
  `doctor_payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `doctor_id` int(11) DEFAULT NULL,
  `doctor_payment_amount` varchar(100) DEFAULT NULL,
  `doctor_payment_date` varchar(100) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`doctor_payment_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `doctor_payment` */

/*Table structure for table `facility` */

DROP TABLE IF EXISTS `facility`;

CREATE TABLE `facility` (
  `facility_id` int(11) NOT NULL AUTO_INCREMENT,
  `petsitting_id` int(11) DEFAULT NULL,
  `service` varchar(100) DEFAULT NULL,
  `facility_des` varchar(100) DEFAULT NULL,
  `facility_image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`facility_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `facility` */

insert  into `facility`(`facility_id`,`petsitting_id`,`service`,`facility_des`,`facility_image`) values 
(1,1,'serjrhn','qqs','static/7e6727eb-ac5b-4b31-9d02-a281aac8ca35surya.jpg');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `feedback_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

/*Table structure for table `fees` */

DROP TABLE IF EXISTS `fees`;

CREATE TABLE `fees` (
  `fees_id` int(11) NOT NULL AUTO_INCREMENT,
  `doctor_id` int(11) DEFAULT NULL,
  `fees` varchar(100) DEFAULT NULL,
  `fees_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`fees_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `fees` */

insert  into `fees`(`fees_id`,`doctor_id`,`fees`,`fees_date`) values 
(1,1,'1500','2024-12-26');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `user_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`user_name`,`password`,`user_type`) values 
(1,'rono','rono1234','doctor'),
(2,'grand','grand1234','shop'),
(3,'trix','trix1234','pending'),
(4,'admin','admin123','admin'),
(5,'arsha','arsha11','user'),
(6,'chumi','chumi','pet_sitting'),
(7,'hththt','saraha123','pending');

/*Table structure for table `pet` */

DROP TABLE IF EXISTS `pet`;

CREATE TABLE `pet` (
  `pet_id` int(11) NOT NULL AUTO_INCREMENT,
  `pet_shop_id` int(11) DEFAULT NULL,
  `pet_name` varchar(100) DEFAULT NULL,
  `pet_type` varchar(100) DEFAULT NULL,
  `pet_breed` varchar(100) DEFAULT NULL,
  `pet_age` varchar(100) DEFAULT NULL,
  `pet_gender` varchar(100) DEFAULT NULL,
  `pet_vaccination_status` varchar(100) DEFAULT NULL,
  `pet_image` varchar(1000) DEFAULT NULL,
  `pet_price` varchar(100) DEFAULT NULL,
  `pet_stock` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pet_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `pet` */

insert  into `pet`(`pet_id`,`pet_shop_id`,`pet_name`,`pet_type`,`pet_breed`,`pet_age`,`pet_gender`,`pet_vaccination_status`,`pet_image`,`pet_price`,`pet_stock`) values 
(1,1,'asdfg','wesdrf','qwer','2 year','male','wert','static/e50d8f21-6d96-461c-838e-2b4de7141c94beagle.jpg','40000','2');

/*Table structure for table `pet_child` */

DROP TABLE IF EXISTS `pet_child`;

CREATE TABLE `pet_child` (
  `pet_child_id` int(11) NOT NULL AUTO_INCREMENT,
  `pet_master_id` int(11) DEFAULT NULL,
  `pet_id` int(11) DEFAULT NULL,
  `pet_child_quantity` varchar(100) DEFAULT NULL,
  `pet_child_amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pet_child_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `pet_child` */

insert  into `pet_child`(`pet_child_id`,`pet_master_id`,`pet_id`,`pet_child_quantity`,`pet_child_amount`) values 
(1,1,1,'1','40000'),
(2,2,1,'1','40000'),
(3,2,1,'1','40000');

/*Table structure for table `pet_master` */

DROP TABLE IF EXISTS `pet_master`;

CREATE TABLE `pet_master` (
  `pet_master_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `pet_master_total` varchar(100) DEFAULT NULL,
  `pet_master_date` varchar(100) DEFAULT NULL,
  `pet_master_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pet_master_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `pet_master` */

insert  into `pet_master`(`pet_master_id`,`user_id`,`pet_master_total`,`pet_master_date`,`pet_master_status`) values 
(1,1,'40000','2024-12-26','paid'),
(2,1,'80000','2024-12-26','paid');

/*Table structure for table `pet_payment` */

DROP TABLE IF EXISTS `pet_payment`;

CREATE TABLE `pet_payment` (
  `pet_payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `pet_master_id` int(11) DEFAULT NULL,
  `pet_payment_amount` varchar(100) DEFAULT NULL,
  `pet_payment_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pet_payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `pet_payment` */

insert  into `pet_payment`(`pet_payment_id`,`pet_master_id`,`pet_payment_amount`,`pet_payment_date`) values 
(1,1,'40000.0','2024-12-26'),
(2,2,'160000.0','2024-12-26');

/*Table structure for table `pet_shop` */

DROP TABLE IF EXISTS `pet_shop`;

CREATE TABLE `pet_shop` (
  `pet_shop_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `shop_name` varchar(100) DEFAULT NULL,
  `shop_email` varchar(100) DEFAULT NULL,
  `shop_phone` varchar(100) DEFAULT NULL,
  `shop_place` varchar(100) DEFAULT NULL,
  `shop_address` varchar(100) DEFAULT NULL,
  `shop_lisence` varchar(100) DEFAULT NULL,
  `shop_lisence_image` varchar(10000) DEFAULT NULL,
  PRIMARY KEY (`pet_shop_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `pet_shop` */

insert  into `pet_shop`(`pet_shop_id`,`login_id`,`shop_name`,`shop_email`,`shop_phone`,`shop_place`,`shop_address`,`shop_lisence`,`shop_lisence_image`) values 
(1,2,'Grand ','grand@gmail.com','1234567890','Vadanappilly','Grand Paranthan Complex',NULL,NULL),
(2,3,'Trix','trix@gmail.com','4567898761','Kodungallur','Trix Kodungallur',NULL,NULL);

/*Table structure for table `pet_show` */

DROP TABLE IF EXISTS `pet_show`;

CREATE TABLE `pet_show` (
  `pet_show_id` int(11) NOT NULL AUTO_INCREMENT,
  `show_id` int(11) DEFAULT NULL,
  `show_name` varchar(1000) DEFAULT NULL,
  `show_participation` varchar(1000) DEFAULT NULL,
  `show_place` varchar(1000) DEFAULT NULL,
  `show_date` varchar(1000) DEFAULT NULL,
  `show_time` varchar(1000) DEFAULT NULL,
  `show_status` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`pet_show_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `pet_show` */

insert  into `pet_show`(`pet_show_id`,`show_id`,`show_name`,`show_participation`,`show_place`,`show_date`,`show_time`,`show_status`) values 
(1,1,'wow','Healthiest Pet','Swaraj Round','2024-12-31','18:00','Pendind');

/*Table structure for table `pet_show_pet` */

DROP TABLE IF EXISTS `pet_show_pet`;

CREATE TABLE `pet_show_pet` (
  `pet_show_pet_id` int(11) NOT NULL AUTO_INCREMENT,
  `pet_show_id` int(11) DEFAULT NULL,
  `show_pet_breed` varchar(1000) DEFAULT NULL,
  `show_pet_age` varchar(1000) DEFAULT NULL,
  `show_pet_gender` varchar(1000) DEFAULT NULL,
  `show_pet_color_pattern` varchar(1000) DEFAULT NULL,
  `show_pet_size` varchar(100) DEFAULT NULL,
  `show_pet_weight` varchar(1000) DEFAULT NULL,
  `show_pet_coat_type` varchar(1000) DEFAULT NULL,
  `show_pet_feature` varchar(1000) DEFAULT NULL,
  `show_pet_owner_name` varchar(1000) DEFAULT NULL,
  `show_pet_image` varchar(2000) DEFAULT NULL,
  `show_qr_code` varchar(30000) DEFAULT NULL,
  `show_pet_name` varchar(1000) DEFAULT NULL,
  `show_pet_type` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`pet_show_pet_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `pet_show_pet` */

insert  into `pet_show_pet`(`pet_show_pet_id`,`pet_show_id`,`show_pet_breed`,`show_pet_age`,`show_pet_gender`,`show_pet_color_pattern`,`show_pet_size`,`show_pet_weight`,`show_pet_coat_type`,`show_pet_feature`,`show_pet_owner_name`,`show_pet_image`,`show_qr_code`,`show_pet_name`,`show_pet_type`) values 
(1,1,'Hound','2','Male','Black and Tan','Small To Medium','10 kg','Patterned coat','The beagle moderate size','Miya','static/3312d5cc-a166-4a33-92d0-dc0529ed9936beagle.jpg','static/qrcode/Hound.png','Beagle','Purebred');

/*Table structure for table `pet_sitting` */

DROP TABLE IF EXISTS `pet_sitting`;

CREATE TABLE `pet_sitting` (
  `petsitting_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `petsitting_name` varchar(100) DEFAULT NULL,
  `owner_name` varchar(100) DEFAULT NULL,
  `petsitting_lisence` varchar(1000) DEFAULT NULL,
  `established_date` varchar(100) DEFAULT NULL,
  `petsitting_email` varchar(100) DEFAULT NULL,
  `petsitting_phone` varchar(100) DEFAULT NULL,
  `street_address` varchar(100) DEFAULT NULL,
  `petsitting_city` varchar(100) DEFAULT NULL,
  `petsitting_state` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`petsitting_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `pet_sitting` */

insert  into `pet_sitting`(`petsitting_id`,`login_id`,`petsitting_name`,`owner_name`,`petsitting_lisence`,`established_date`,`petsitting_email`,`petsitting_phone`,`street_address`,`petsitting_city`,`petsitting_state`) values 
(1,6,'Petcare','sumi','static/d9a0a069-d5ed-40c0-8e9b-19b96cbd8748grp.jpg','2025-02-06','ammu@gmail.com','9876543331','ammu house','thrissur','kerala'),
(2,7,'Petwall','k','static/6919d568-9db3-48d0-8146-c82a95b4b34cpetcare_login_bg.png','2025-01-31','uuu@gmail.com','9876890089','abc house','thrissur','kerala');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(100) DEFAULT NULL,
  `product_price` varchar(100) DEFAULT NULL,
  `product_stock` varchar(100) DEFAULT NULL,
  `product_image` varchar(100) DEFAULT NULL,
  `pet_shop_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`product_name`,`product_price`,`product_stock`,`product_image`,`pet_shop_id`) values 
(1,'asdfg','100','5','static/e079db5d-a395-4f42-a597-71aac4b3c98bfootprint_petcare.png',1);

/*Table structure for table `product_child` */

DROP TABLE IF EXISTS `product_child`;

CREATE TABLE `product_child` (
  `product_child_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_master_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `product_child_quantity` varchar(100) DEFAULT NULL,
  `product_child_amount` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`product_child_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `product_child` */

insert  into `product_child`(`product_child_id`,`product_master_id`,`product_id`,`product_child_quantity`,`product_child_amount`) values 
(1,1,1,'1','100'),
(2,1,1,'1','100'),
(3,1,1,'1','100');

/*Table structure for table `product_master` */

DROP TABLE IF EXISTS `product_master`;

CREATE TABLE `product_master` (
  `product_master_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `product_master_total` varchar(100) DEFAULT NULL,
  `product_master_date` varchar(100) DEFAULT NULL,
  `product_master_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`product_master_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `product_master` */

insert  into `product_master`(`product_master_id`,`user_id`,`product_master_total`,`product_master_date`,`product_master_status`) values 
(1,1,'300','2024-12-26','pending');

/*Table structure for table `product_payment` */

DROP TABLE IF EXISTS `product_payment`;

CREATE TABLE `product_payment` (
  `product_payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_master_id` int(11) DEFAULT NULL,
  `product_payment_amount` varchar(100) DEFAULT NULL,
  `product_payment_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`product_payment_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `product_payment` */

/*Table structure for table `proposal` */

DROP TABLE IF EXISTS `proposal`;

CREATE TABLE `proposal` (
  `proposal_id` int(11) NOT NULL AUTO_INCREMENT,
  `request_id` int(11) DEFAULT NULL,
  `proposal_amount` varchar(100) DEFAULT NULL,
  `proposal_status` varchar(100) DEFAULT NULL,
  `proposal_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`proposal_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `proposal` */

insert  into `proposal`(`proposal_id`,`request_id`,`proposal_amount`,`proposal_status`,`proposal_date`) values 
(1,1,'1000','pending','2025-02-14');

/*Table structure for table `proposal_payment` */

DROP TABLE IF EXISTS `proposal_payment`;

CREATE TABLE `proposal_payment` (
  `proposal_payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `proposal_id` int(11) DEFAULT NULL,
  `payment_amount` varchar(100) DEFAULT NULL,
  `payment_status` varchar(100) DEFAULT NULL,
  `payment_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`proposal_payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `proposal_payment` */

insert  into `proposal_payment`(`proposal_payment_id`,`proposal_id`,`payment_amount`,`payment_status`,`payment_date`) values 
(1,1,'1000','paid','14-02-2025');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `service_type` varchar(100) DEFAULT NULL,
  `request_des` varchar(100) DEFAULT NULL,
  `request_date` varchar(100) DEFAULT NULL,
  `request_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`request_id`,`user_id`,`service_type`,`request_des`,`request_date`,`request_status`) values 
(1,1,'bhgy','ghtfrtdts','13-02-2025','accept');

/*Table structure for table `slot` */

DROP TABLE IF EXISTS `slot`;

CREATE TABLE `slot` (
  `slot_id` int(11) NOT NULL AUTO_INCREMENT,
  `appointment_id` int(11) DEFAULT NULL,
  `slot_day` varchar(100) DEFAULT NULL,
  `slot_time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`slot_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `slot` */

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `user_fname` varchar(100) DEFAULT NULL,
  `user_lname` varchar(100) DEFAULT NULL,
  `user_phone` varchar(100) DEFAULT NULL,
  `user_email` varchar(100) DEFAULT NULL,
  `user_place` varchar(100) DEFAULT NULL,
  `user_address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`user_fname`,`user_lname`,`user_phone`,`user_email`,`user_place`,`user_address`) values 
(1,5,'Arsha','Sudersanan','9876543210','arshasudersanan@gmail.com','Engandiyur','Memby House');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

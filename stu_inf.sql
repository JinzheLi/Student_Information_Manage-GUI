/*
SQLyog 企业版 - MySQL GUI v7.14 
MySQL - 5.7.25 : Database - stu_inf
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`stu_inf` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `stu_inf`;

/*Table structure for table `stu` */

DROP TABLE IF EXISTS `stu`;

CREATE TABLE `stu` (
  `id` char(12) NOT NULL,
  `name` varchar(10) NOT NULL,
  `age` tinyint(3) unsigned NOT NULL,
  `sex` enum('男','女') NOT NULL,
  `Sdept` varchar(5) NOT NULL,
  `profession` varchar(3) NOT NULL,
  `classid` tinyint(3) unsigned NOT NULL,
  `grade` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `stu` */

insert  into `stu`(`id`,`name`,`age`,`sex`,`Sdept`,`profession`,`classid`,`grade`) values ('201707010100','李四',19,'男','理学院','信计',1,17),('201707010119','李金哲',20,'男','理学院','信计',1,17),('201707010120','代森',20,'男','理学院','信计',1,17);

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user` varchar(8) NOT NULL,
  `password` varchar(16) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user` (`user`)
) ENGINE=InnoDB AUTO_INCREMENT=814055 DEFAULT CHARSET=utf8;

/*Data for the table `users` */

insert  into `users`(`id`,`user`,`password`) values (123,'李四','123'),(814054,'张三','123456');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;

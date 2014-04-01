-- phpMyAdmin SQL Dump
-- version 4.0.6deb1
-- http://www.phpmyadmin.net
--
-- Client: localhost
-- Généré le: Mar 01 Avril 2014 à 20:22
-- Version du serveur: 5.5.35-0ubuntu0.13.10.2
-- Version de PHP: 5.5.3-1ubuntu2.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `boe`
--

-- --------------------------------------------------------

--
-- Structure de la table `client`
--

CREATE TABLE IF NOT EXISTS `client` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `company_name` varchar(50) NOT NULL,
  `email_address` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=38 ;

--
-- Contenu de la table `client`
--

INSERT INTO `client` (`id`, `company_name`, `email_address`) VALUES
(1, 'Eucles Daily', 'benoit.minard@gmail.com'),
(2, 'BMDeveloppementT', 'benoit.minard@gmail.com'),
(3, 'dolead', 'test@gmail.com'),
(4, 'dolead', 'test@gmail.com'),
(5, 'PasDolead123dsds', 'pas_test@gmail.com'),
(6, 'dolead', 'test@gmail.com'),
(7, 'dolead', 'test@gmail.com'),
(8, 'dolead2', 'test@gmail.com'),
(9, 'dolead2', 'test@gmail.com'),
(10, 'dolead2', 'test@gmail.com'),
(11, 'dolead2', 'test@gmail.com'),
(12, 'dolead2', 'test@gmail.com'),
(13, 'dolead2', 'test@gmail.com'),
(14, 'dolead2', 'test@gmail.com'),
(15, 'dolead2', 'test@gmail.com'),
(16, 'dolead2', 'test@gmail.com'),
(17, 'dolead2', 'test@gmail.com'),
(18, 'dolead555', 'test@gmail.com'),
(19, 'dolead555', 'test@gmail.com'),
(20, 'dolead2', 'test@gmail.com'),
(21, 'dolead2', 'test@gmail.com'),
(22, 'dolead2', 'test@gmail.com'),
(23, 'dolead2', 'test@gmail.com'),
(24, 'dolead2', 'test@gmail.com'),
(25, 'dolead2', 'test@gmail.com'),
(26, 'dolead1245555', 'test@gmail.com'),
(27, 'Test', 'test@yopmail.com'),
(28, 'Test', 'test@yopmail.com'),
(29, 'Ceci est un test', 'Encore un test'),
(30, 'Ceci est un test', 'Encore un test'),
(31, 'Eucles Daily', 'benoit.minard@gmail.com'),
(32, 'Eucles Daily', 'benoit.minard@gmail.com'),
(33, 'Eucles Daily1', 'benoit.minard@gmail.com'),
(34, 'dzad', 'dza@de.com'),
(35, 'Eucles Daily4', 'benoit.minard@gmail1.com'),
(36, 'Eucles Daily4', 'benoit.minard@gmail1.com'),
(37, 'Test', 'benoit.minard@gmail1.com');

-- --------------------------------------------------------

--
-- Structure de la table `deliverer`
--

CREATE TABLE IF NOT EXISTS `deliverer` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `company_name` varchar(50) NOT NULL,
  `email_address` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

--
-- Contenu de la table `deliverer`
--

INSERT INTO `deliverer` (`id`, `company_name`, `email_address`) VALUES
(1, 'PasDolead123', 'pas1_test@gmail.com'),
(2, 'delivrer1', 'testdeliver@gmail.com'),
(3, 'delivrer2', 'testdeliver@gmail.com'),
(4, 'BMDeveloppement', 'test@yopmail.com');

-- --------------------------------------------------------

--
-- Structure de la table `delivery`
--

CREATE TABLE IF NOT EXISTS `delivery` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `distribution_round_id` int(10) unsigned NOT NULL,
  `point_of_sale_id` int(10) unsigned NOT NULL,
  `date` datetime NOT NULL,
  `price` float(8,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `distribution_round_id` (`distribution_round_id`),
  KEY `point_of_sale_id` (`point_of_sale_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Contenu de la table `delivery`
--

INSERT INTO `delivery` (`id`, `distribution_round_id`, `point_of_sale_id`, `date`, `price`) VALUES
(1, 1, 2, '2014-04-22 10:06:55', 11.10);

-- --------------------------------------------------------

--
-- Structure de la table `distribution_round`
--

CREATE TABLE IF NOT EXISTS `distribution_round` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `deliverer_id` int(10) unsigned NOT NULL,
  `name` varchar(50) NOT NULL,
  `cost` float(8,2) NOT NULL,
  `unitary_cost` float(8,2) NOT NULL,
  `schedule` varchar(500) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `deliverer_id` (`deliverer_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Contenu de la table `distribution_round`
--

INSERT INTO `distribution_round` (`id`, `deliverer_id`, `name`, `cost`, `unitary_cost`, `schedule`) VALUES
(1, 3, 'Tournée de merle', 55.95, 0.10, '{''monday'': ''true''}'),
(2, 1, 'Tournée de samir', 14.00, 0.00, '{''monday'': ''false''}'),
(3, 2, 'Barbes Tour Eiffel', 15.00, 0.99, 'QQ chose comme ça');

-- --------------------------------------------------------

--
-- Structure de la table `newspaper`
--

CREATE TABLE IF NOT EXISTS `newspaper` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `press_title_id` int(10) unsigned NOT NULL,
  `client_id` int(10) unsigned NOT NULL,
  `delivery_id` int(10) unsigned NOT NULL,
  `point_of_sale_id` int(10) unsigned NOT NULL,
  `date` datetime NOT NULL,
  `price` float(5,2) NOT NULL,
  `supplier_cost` float(5,2) NOT NULL,
  `royalty_cost` float(5,2) DEFAULT NULL,
  `paging` int(11) DEFAULT NULL,
  `unsold` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `point_of_sale_id` (`point_of_sale_id`),
  KEY `delivery_id` (`delivery_id`),
  KEY `client_id` (`client_id`),
  KEY `press_title_id` (`press_title_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Contenu de la table `newspaper`
--

INSERT INTO `newspaper` (`id`, `press_title_id`, `client_id`, `delivery_id`, `point_of_sale_id`, `date`, `price`, `supplier_cost`, `royalty_cost`, `paging`, `unsold`) VALUES
(1, 1, 1, 1, 1, '2013-04-12 11:50:00', 1.26, 1.44, 0.21, 14, 0),
(2, 2, 2, 1, 3, '2013-04-12 11:50:00', 1.26, 1.44, 0.21, 14, 0);

-- --------------------------------------------------------

--
-- Structure de la table `order`
--

CREATE TABLE IF NOT EXISTS `order` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `press_title_id` int(10) unsigned NOT NULL,
  `point_of_sale_id` int(10) unsigned NOT NULL,
  `order_date` datetime NOT NULL,
  `delivery_date` datetime NOT NULL,
  `quantity` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `point_of_sale_id` (`point_of_sale_id`),
  KEY `press_title_id` (`press_title_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Contenu de la table `order`
--

INSERT INTO `order` (`id`, `press_title_id`, `point_of_sale_id`, `order_date`, `delivery_date`, `quantity`) VALUES
(1, 1, 2, '2014-05-29 10:00:00', '2014-05-29 10:30:00', 38),
(2, 2, 3, '2014-05-30 10:00:00', '2014-05-30 10:30:00', 54);

-- --------------------------------------------------------

--
-- Structure de la table `point_of_sale`
--

CREATE TABLE IF NOT EXISTS `point_of_sale` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `client_id` int(10) unsigned NOT NULL,
  `delivery_price` float(8,2) NOT NULL,
  `address` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `zip_code` int(11) NOT NULL,
  `additional_data` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `client_id` (`client_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=11 ;

--
-- Contenu de la table `point_of_sale`
--

INSERT INTO `point_of_sale` (`id`, `client_id`, `delivery_price`, `address`, `city`, `zip_code`, `additional_data`) VALUES
(1, 18, 1.75, '26 rue Beaurepaire', 'Paris', 75010, 'Truc'),
(2, 4, 2.00, '3 rue de crussol', 'Paris', 75010, ''),
(3, 4, 2.25, '26 rue Beaurepaire', 'Paris', 75010, ''),
(4, 5, 0.88, 'uio', 'Paris', 75010, ''),
(5, 5, 0.88, 'uio', 'Paris', 75010, ''),
(6, 30, 0.88, '3 rue Voltaire', 'London', 75011, 'Aucun'),
(7, 1, 0.00, 'fez', 'fez', 0, ''),
(8, 1, 0.88, '3 rue Voltaire', 'London', 75010, ''),
(9, 1, 0.88, '3 rue Voltaire', 'London', 75010, ''),
(10, 1, 0.99, 'jkl', 'njk', 0, '');

-- --------------------------------------------------------

--
-- Structure de la table `point_of_sale_distribution_round`
--

CREATE TABLE IF NOT EXISTS `point_of_sale_distribution_round` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `point_of_sale_id` int(10) unsigned NOT NULL,
  `distribution_round_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `distribution_round_id` (`distribution_round_id`),
  KEY `point_of_sale_id` (`point_of_sale_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

--
-- Contenu de la table `point_of_sale_distribution_round`
--

INSERT INTO `point_of_sale_distribution_round` (`id`, `point_of_sale_id`, `distribution_round_id`) VALUES
(2, 1, 1);

-- --------------------------------------------------------

--
-- Structure de la table `press_title`
--

CREATE TABLE IF NOT EXISTS `press_title` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `supplier_id` int(10) unsigned NOT NULL,
  `name` varchar(50) NOT NULL,
  `supplier_cost` float(5,2) NOT NULL,
  `royalty_cost` float(5,2) DEFAULT NULL,
  `paging` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `supplier_id` (`supplier_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

--
-- Contenu de la table `press_title`
--

INSERT INTO `press_title` (`id`, `supplier_id`, `name`, `supplier_cost`, `royalty_cost`, `paging`) VALUES
(1, 1, 'el watan Evolution', 1.12, 0.21, 38),
(2, 1, 'el watan', 1.02, 0.21, 40),
(3, 3, 'el watan', 1.02, 0.21, 38),
(4, 1, 'el watan', 1.02, 0.21, 38),
(5, 1, 'NY Times', 0.98, 0.40, 75);

-- --------------------------------------------------------

--
-- Structure de la table `supplier`
--

CREATE TABLE IF NOT EXISTS `supplier` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `company_name` varchar(50) NOT NULL,
  `email_address` varchar(50) NOT NULL,
  `report` tinyint(1) NOT NULL DEFAULT '0',
  `reporting_hour` time NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

--
-- Contenu de la table `supplier`
--

INSERT INTO `supplier` (`id`, `company_name`, `email_address`, `report`, `reporting_hour`) VALUES
(1, 'mycompany', 'mail@mycompany.com', 0, '00:20:13'),
(2, 'mycompany', 'mail@mycompany.co1', 1, '00:20:13'),
(3, 'pipo', 'pouet', 1, '12:00:00'),
(4, 'pipo', 'pouet', 1, '12:00:00'),
(5, 'mycompany', 'benoit.minard@gmail.com', 1, '10:20:13');

-- --------------------------------------------------------

--
-- Structure de la table `supplier_price`
--

CREATE TABLE IF NOT EXISTS `supplier_price` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `press_title_id` int(10) unsigned NOT NULL,
  `client_id` int(10) unsigned NOT NULL,
  `value` float(5,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `press_title_id` (`press_title_id`),
  KEY `client_id` (`client_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

--
-- Contenu de la table `supplier_price`
--

INSERT INTO `supplier_price` (`id`, `press_title_id`, `client_id`, `value`) VALUES
(1, 2, 3, 14.06),
(2, 1, 1, 14.06),
(3, 1, 1, 55.62),
(4, 2, 3, 14.06),
(5, 2, 3, 14.06),
(6, 2, 3, 14.06);

--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `delivery`
--
ALTER TABLE `delivery`
  ADD CONSTRAINT `delivery_ibfk_2` FOREIGN KEY (`point_of_sale_id`) REFERENCES `point_of_sale` (`id`),
  ADD CONSTRAINT `delivery_ibfk_1` FOREIGN KEY (`distribution_round_id`) REFERENCES `distribution_round` (`id`);

--
-- Contraintes pour la table `distribution_round`
--
ALTER TABLE `distribution_round`
  ADD CONSTRAINT `distribution_round_ibfk_1` FOREIGN KEY (`deliverer_id`) REFERENCES `deliverer` (`id`);

--
-- Contraintes pour la table `newspaper`
--
ALTER TABLE `newspaper`
  ADD CONSTRAINT `newspaper_ibfk_4` FOREIGN KEY (`delivery_id`) REFERENCES `delivery` (`id`),
  ADD CONSTRAINT `newspaper_ibfk_1` FOREIGN KEY (`press_title_id`) REFERENCES `press_title` (`id`),
  ADD CONSTRAINT `newspaper_ibfk_2` FOREIGN KEY (`client_id`) REFERENCES `client` (`id`),
  ADD CONSTRAINT `newspaper_ibfk_3` FOREIGN KEY (`point_of_sale_id`) REFERENCES `point_of_sale` (`id`);

--
-- Contraintes pour la table `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `order_ibfk_2` FOREIGN KEY (`point_of_sale_id`) REFERENCES `point_of_sale` (`id`),
  ADD CONSTRAINT `order_ibfk_1` FOREIGN KEY (`press_title_id`) REFERENCES `press_title` (`id`);

--
-- Contraintes pour la table `point_of_sale`
--
ALTER TABLE `point_of_sale`
  ADD CONSTRAINT `point_of_sale_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `client` (`id`);

--
-- Contraintes pour la table `point_of_sale_distribution_round`
--
ALTER TABLE `point_of_sale_distribution_round`
  ADD CONSTRAINT `point_of_sale_distribution_round_ibfk_2` FOREIGN KEY (`distribution_round_id`) REFERENCES `distribution_round` (`id`),
  ADD CONSTRAINT `point_of_sale_distribution_round_ibfk_1` FOREIGN KEY (`point_of_sale_id`) REFERENCES `point_of_sale` (`id`);

--
-- Contraintes pour la table `press_title`
--
ALTER TABLE `press_title`
  ADD CONSTRAINT `press_title_ibfk_1` FOREIGN KEY (`supplier_id`) REFERENCES `supplier` (`id`);

--
-- Contraintes pour la table `supplier_price`
--
ALTER TABLE `supplier_price`
  ADD CONSTRAINT `supplier_price_ibfk_2` FOREIGN KEY (`client_id`) REFERENCES `client` (`id`),
  ADD CONSTRAINT `supplier_price_ibfk_1` FOREIGN KEY (`press_title_id`) REFERENCES `press_title` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
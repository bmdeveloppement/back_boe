-- phpMyAdmin SQL Dump
-- version 4.0.6deb1
-- http://www.phpmyadmin.net
--
-- Client: localhost
-- Généré le: Sam 05 Avril 2014 à 16:49
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
-- Structure de la table `delivery`
--

CREATE TABLE IF NOT EXISTS `delivery` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `distribution_round_id` int(10) unsigned NOT NULL,
  `point_of_sale_id` int(10) unsigned NOT NULL,
  `date` datetime NOT NULL,
  `distribution_round_cost` float NOT NULL,
  `price` float(8,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `distribution_round_id` (`distribution_round_id`),
  KEY `point_of_sale_id` (`point_of_sale_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Contenu de la table `delivery`
--

INSERT INTO `delivery` (`id`, `distribution_round_id`, `point_of_sale_id`, `date`, `distribution_round_cost`, `price`) VALUES
(1, 1, 2, '2014-04-22 10:06:55', 0, 11.10);

--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `delivery`
--
ALTER TABLE `delivery`
  ADD CONSTRAINT `delivery_ibfk_1` FOREIGN KEY (`distribution_round_id`) REFERENCES `distribution_round` (`id`),
  ADD CONSTRAINT `delivery_ibfk_2` FOREIGN KEY (`point_of_sale_id`) REFERENCES `point_of_sale` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
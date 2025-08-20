-- 데이터베이스 생성 (이미 존재하면 넘어감)
CREATE DATABASE IF NOT EXISTS `mydatabase` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE `mydatabase`;

CREATE TABLE `contacts_contact` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `email` VARCHAR(254) NULL,
    `phone_number` VARCHAR(20) NOT NULL,
    `company` VARCHAR(100) NULL,
    `job_title` VARCHAR(100) NULL,
    `memo` TEXT NULL,
    `profile_photo_url` VARCHAR(200) NULL,
    `address` VARCHAR(255) NULL,
    `birthday` DATE NULL,
    `website` VARCHAR(200) NULL,
    `created_at` DATETIME NOT NULL,
    `updated_at` DATETIME NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE `contacts_label` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `contact_id` INT NOT NULL,
    CONSTRAINT `fk_contact`
        FOREIGN KEY (`contact_id`) 
        REFERENCES `contacts_contact`(`id`) 
        ON DELETE CASCADE,
    UNIQUE KEY `unique_contact_label_name` (`contact_id`, `name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

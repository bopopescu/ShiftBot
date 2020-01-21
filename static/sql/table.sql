CREATE TABLE members (
  slackID varchar(10) NOT NULL,
  _name varchar(128) NOT NULL,
  _kana varchar(128) DEFAULT NULL,
  _grade char(10) NOT NULL,
  /*'kanaOrder_grade' int(11) unsigned DEFAULT NULL,*/
  PRIMARY KEY (slackID)
) ENGINE=InnoDB;

CREATE TABLE trash (
    slackID varchar(10) NOT NULL,
    _room char(10) NOT NULL,
    _order int(11) DEFAULT NULL,
    _onDuty bit(1) NOT NULL,
    _cursor bit(1) NOT NULL,
    PRIMARY KEY (slackID)
) ENGINE=InnoDB;

CREATE TABLE minutes (
    slackID varchar(10) NOT NULL,
    _order int(11) DEFAULT NULL,
    _onDuty bit(1) NOT NULL,
    _cursor bit(1) NOT NULL,
    PRIMARY KEY (slackID)
) ENGINE=InnoDB;

INSERT INTO members (slackID, _name, _kana, _grade)
VALUES
	('U72B60S3H','中野','なかの','m1'),
	('UDBS25RJ9','伊藤','いとう','b4'),
	('UDBLHCZ50','佐藤','さとう','b4'),
	('ULKF54DEH','勝又','かつまた','b3'),
	('UL4KHGNM6','庵谷','いほりや','b3'),
	('U73K61E7M','斎藤','さいとう','m1'),
	('UDCN58XST','村田','むらた','b4'),
	('U726HGZMZ','梅田','うめだ','m1'),
	('UDBHSNXJP','永野','ながの','b4'),
	('ULMK1UHJS','清水','しみず','b3'),
	('UKT7RN32P','若月','わかつき','b3'),
	('UDAU6U5A4','誓山','ちかやま','b4'),
	('UDAU6Q064','鈴木','すずき','b4'),
	('UNYLCCNSU','陳','ちぇん','m1');

INSERT INTO trash (slackID, _room, _order, _onDuty, _cursor)
VALUES
    ('U72B60S3H','2525',8,b'0',b'0'),
    ('UDBS25RJ9','2525',1,b'0',b'0'),
    ('UDBLHCZ50','2525',5,b'0',b'0'),
    ('ULKF54DEH','2525',3,b'0',b'0'),
    ('UL4KHGNM6','2525',2,b'0',b'0'),
    ('U73K61E7M','2525',4,b'0',b'0'),
    ('UDCN58XST','2721',1,b'0',b'0'),
    ('U726HGZMZ','2721',4,b'0',b'0'),
    ('UDBHSNXJP','2525',9,b'0',b'0'),
    ('ULMK1UHJS','2721',2,b'0',b'0'),
    ('UKT7RN32P','2721',3,b'0',b'0'),
    ('UDAU6U5A4','2721',5,b'0',b'0'),
    ('UDAU6Q064','2525',6,b'0',b'0'),
    ('UNYLCCNSU','2525',7,b'0',b'0');

INSERT INTO minutes (slackID, _order, _onDuty, _cursor)
VALUES
    ('U72B60S3H',0,b'0',b'0'),
    ('UDBS25RJ9',0,b'0',b'0'),
    ('UDBLHCZ50',0,b'0',b'0'),
    ('ULKF54DEH',0,b'0',b'0'),
    ('UL4KHGNM6',0,b'0',b'0'),
    ('U73K61E7M',0,b'0',b'0'),
    ('UDCN58XST',0,b'0',b'0'),
    ('U726HGZMZ',0,b'0',b'0'),
    ('UDBHSNXJP',0,b'0',b'0'),
    ('ULMK1UHJS',0,b'0',b'0'),
    ('UKT7RN32P',0,b'0',b'0'),
    ('UDAU6U5A4',0,b'0',b'0'),
    ('UDAU6Q064',0,b'0',b'0'),
    ('UNYLCCNSU',0,b'0',b'0');
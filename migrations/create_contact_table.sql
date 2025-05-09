CREATE TABLE 'contacts' (
	'id' UUID NOT NULL,
    'phone_number' varchar(150) NOT NULL,
	'email' varchar(150) NOT NULL,
	'name' varchar(150) NOT NULL,
	'createdAt' datetime NOT NULL,
	'updatedAt' datetime NOT NULL,
	CONSTRAINT 'contacts_id' PRIMARY KEY('id'),
	CONSTRAINT 'contacts_name' UNIQUE('name'),
	CONSTRAINT 'contacts_phone_number' UNIQUE('phone_number'),
	CONSTRAINT 'contacts_email' UNIQUE('email'),
);

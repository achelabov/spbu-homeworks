-- +goose Up
-- +goose StatementBegin
SELECT 'up SQL query';
-- +goose StatementEnd
CREATE TYPE vaccinations_type AS ENUM ('fury', 'distemper');

CREATE TABLE vaccinations 
(
	pet_id			INTEGER			  NOT NULL,
	vaccination		vaccinations_type NOT NULL,
	date			TIMESTAMP		  NOT NULL, 
	document_base64 TEXT			  NOT NULL,
	CONSTRAINT pet_fk 
        FOREIGN KEY (pet_id)
            REFERENCES Pet (Pet_ID)
);
-- +goose Down
-- +goose StatementBegin
SELECT 'down SQL query';
-- +goose StatementEnd
DROP TABLE vaccinations;
DROP TYPE vaccinations_type;

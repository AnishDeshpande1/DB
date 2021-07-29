drop table reservations;
drop table venues;
drop table users;

CREATE TABLE reservations (
    reservationid integer NOT NULL,
    venueid integer NOT NULL,
    userid integer NOT NULL,
    starttime timestamp without time zone NOT NULL,
    slots integer NOT NULL
);

CREATE TABLE venues (
    venueid integer NOT NULL,
    name character varying(100) NOT NULL,
    usercost numeric NOT NULL,
    guestcost numeric NOT NULL,
    investment numeric NOT NULL,
    monthlymaintenance numeric NOT NULL
);


CREATE TABLE users (
    userid integer NOT NULL,
    familyname character varying(200) NOT NULL,
    givenname character varying(200) NOT NULL,
    pincode integer NOT NULL,
    phone character varying(20) NOT NULL,
    recommender integer,
    dateofjoining timestamp without time zone NOT NULL
);



ALTER TABLE ONLY reservations
    ADD CONSTRAINT reservations_pk PRIMARY KEY (reservationid);



ALTER TABLE ONLY venues
    ADD CONSTRAINT venues_pk PRIMARY KEY (venueid);



ALTER TABLE ONLY users
    ADD CONSTRAINT users_pk PRIMARY KEY (userid);



ALTER TABLE ONLY reservations
    ADD CONSTRAINT fk_reservations_venueid FOREIGN KEY (venueid) REFERENCES venues(venueid);



ALTER TABLE ONLY reservations
    ADD CONSTRAINT fk_reservations_userid FOREIGN KEY (userid) REFERENCES users(userid);


ALTER TABLE ONLY users
    ADD CONSTRAINT fk_users_recommender FOREIGN KEY (recommender) REFERENCES users(userid) ON DELETE SET NULL;




CREATE INDEX "reservations.userid_venueid"
  ON reservations
  USING btree
  (userid, venueid);

CREATE INDEX "reservations.venueid_userid"
  ON reservations
  USING btree
  (venueid, userid);

CREATE INDEX "reservations.venueid_starttime"
  ON reservations
  USING btree
  (venueid, starttime);

CREATE INDEX "reservations.userid_starttime"
  ON reservations
  USING btree
  (userid, starttime);

CREATE INDEX "reservations.starttime"
  ON reservations
  USING btree
  (starttime);

CREATE INDEX "users.dateofjoining"
  ON users
  USING btree
  (dateofjoining);

CREATE INDEX "users.recommender"
  ON users
  USING btree
  (recommender);

ANALYZE;

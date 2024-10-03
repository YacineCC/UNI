--
-- PostgreSQL database dump
--

-- Dumped from database version 15.7
-- Dumped by pg_dump version 16.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: bd; Type: SCHEMA; Schema: -; Owner: group_m1_db
--

CREATE SCHEMA bd;


ALTER SCHEMA bd OWNER TO group_m1_db;

--
-- Name: etoiles_t; Type: DOMAIN; Schema: bd; Owner: group_m1_db
--

CREATE DOMAIN bd.etoiles_t AS integer
	CONSTRAINT etoiles_t_check CHECK (((VALUE >= 1) AND (VALUE <= 5)));


ALTER DOMAIN bd.etoiles_t OWNER TO group_m1_db;

--
-- Name: mode_enchainement; Type: TYPE; Schema: bd; Owner: group_m1_db
--

CREATE TYPE bd.mode_enchainement AS ENUM (
    'redpoint',
    'flash',
    'a_vue'
);


ALTER TYPE bd.mode_enchainement OWNER TO group_m1_db;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: blocs; Type: TABLE; Schema: bd; Owner: group_m1_db
--

CREATE TABLE bd.blocs (
    depart_assis boolean DEFAULT false,
    circuit integer,
    id_b integer NOT NULL
);


ALTER TABLE bd.blocs OWNER TO group_m1_db;

--
-- Name: circuits; Type: TABLE; Schema: bd; Owner: group_m1_db
--

CREATE TABLE bd.circuits (
    id_c integer NOT NULL,
    couleur character varying(30),
    secteur integer
);


ALTER TABLE bd.circuits OWNER TO group_m1_db;

--
-- Name: cote; Type: TABLE; Schema: bd; Owner: group_m1_db
--

CREATE TABLE bd.cote (
    cote character varying(3) NOT NULL,
    points_enchainement integer,
    points_flash integer,
    points_vue integer,
    points_fa integer
);


ALTER TABLE bd.cote OWNER TO group_m1_db;

--
-- Name: couennes; Type: TABLE; Schema: bd; Owner: group_m1_db
--

CREATE TABLE bd.couennes (
    id_c integer NOT NULL
);


ALTER TABLE bd.couennes OWNER TO group_m1_db;

--
-- Name: croite; Type: TABLE; Schema: bd; Owner: group_m1_db
--

CREATE TABLE bd.croite (
    id_g integer NOT NULL,
    id_l integer NOT NULL,
    mode bd.mode_enchainement,
    avis_beaute bd.etoiles_t,
    avis_cotation character varying(3)
);


ALTER TABLE bd.croite OWNER TO group_m1_db;

--
-- Name: grimpeurs; Type: TABLE; Schema: bd; Owner: group_m1_db
--

CREATE TABLE bd.grimpeurs (
    id_g integer NOT NULL,
    nom_g character varying(50),
    prenom_g character varying(50),
    ranking integer,
    certifie boolean DEFAULT false
);


ALTER TABLE bd.grimpeurs OWNER TO group_m1_db;

--
-- Name: grimpeurs_id_g_seq; Type: SEQUENCE; Schema: bd; Owner: group_m1_db
--

ALTER TABLE bd.grimpeurs ALTER COLUMN id_g ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME bd.grimpeurs_id_g_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: lignes; Type: TABLE; Schema: bd; Owner: group_m1_db
--

CREATE TABLE bd.lignes (
    id_l integer NOT NULL,
    cotation character varying(3),
    secteur integer,
    nom_l text
);


ALTER TABLE bd.lignes OWNER TO group_m1_db;

--
-- Name: lignes_id_l_seq; Type: SEQUENCE; Schema: bd; Owner: group_m1_db
--

ALTER TABLE bd.lignes ALTER COLUMN id_l ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME bd.lignes_id_l_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: massif; Type: TABLE; Schema: bd; Owner: group_m1_db
--

CREATE TABLE bd.massif (
    id_m integer NOT NULL,
    point_gps integer NOT NULL
);


ALTER TABLE bd.massif OWNER TO group_m1_db;

--
-- Name: media; Type: TABLE; Schema: bd; Owner: group_m1_db
--

CREATE TABLE bd.media (
    id_m integer NOT NULL
);


ALTER TABLE bd.media OWNER TO group_m1_db;

--
-- Name: posts; Type: TABLE; Schema: bd; Owner: group_m1_db
--

CREATE TABLE bd.posts (
    id_p integer NOT NULL,
    text character varying,
    attachements integer
);


ALTER TABLE bd.posts OWNER TO group_m1_db;

--
-- Name: secteurs; Type: TABLE; Schema: bd; Owner: group_m1_db
--

CREATE TABLE bd.secteurs (
    id_s integer NOT NULL,
    point_gps point,
    nom character varying(20)
);


ALTER TABLE bd.secteurs OWNER TO group_m1_db;

--
-- Name: secteurs_id_s_seq; Type: SEQUENCE; Schema: bd; Owner: group_m1_db
--

ALTER TABLE bd.secteurs ALTER COLUMN id_s ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME bd.secteurs_id_s_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: sponsor; Type: TABLE; Schema: bd; Owner: group_m1_db
--

CREATE TABLE bd.sponsor (
    id_s integer NOT NULL,
    nom_marque character varying(50),
    url character varying
);


ALTER TABLE bd.sponsor OWNER TO group_m1_db;

--
-- Name: blocs bloc_pkey; Type: CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.blocs
    ADD CONSTRAINT bloc_pkey PRIMARY KEY (id_b);


--
-- Name: circuits circuits_pkey; Type: CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.circuits
    ADD CONSTRAINT circuits_pkey PRIMARY KEY (id_c);


--
-- Name: cote cote_pkey; Type: CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.cote
    ADD CONSTRAINT cote_pkey PRIMARY KEY (cote);


--
-- Name: couennes couennes_pkey; Type: CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.couennes
    ADD CONSTRAINT couennes_pkey PRIMARY KEY (id_c);


--
-- Name: croite grimpe_pkey; Type: CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.croite
    ADD CONSTRAINT grimpe_pkey PRIMARY KEY (id_g, id_l);


--
-- Name: grimpeurs grimpeur_pkey; Type: CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.grimpeurs
    ADD CONSTRAINT grimpeur_pkey PRIMARY KEY (id_g);


--
-- Name: lignes lignes_pkey; Type: CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.lignes
    ADD CONSTRAINT lignes_pkey PRIMARY KEY (id_l);


--
-- Name: massif massif_pkey; Type: CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.massif
    ADD CONSTRAINT massif_pkey PRIMARY KEY (id_m, point_gps);


--
-- Name: media media_pkey; Type: CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.media
    ADD CONSTRAINT media_pkey PRIMARY KEY (id_m);


--
-- Name: posts posts_pkey; Type: CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (id_p);


--
-- Name: secteurs secteurs_pkey; Type: CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.secteurs
    ADD CONSTRAINT secteurs_pkey PRIMARY KEY (id_s);


--
-- Name: sponsor sponsor_pkey; Type: CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.sponsor
    ADD CONSTRAINT sponsor_pkey PRIMARY KEY (id_s);


--
-- Name: massif unique_point_gps; Type: CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.massif
    ADD CONSTRAINT unique_point_gps UNIQUE (point_gps);


--
-- Name: blocs fk_b; Type: FK CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.blocs
    ADD CONSTRAINT fk_b FOREIGN KEY (id_b) REFERENCES bd.lignes(id_l);


--
-- Name: blocs fk_bloc; Type: FK CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.blocs
    ADD CONSTRAINT fk_bloc FOREIGN KEY (circuit) REFERENCES bd.circuits(id_c);


--
-- Name: lignes fk_cote; Type: FK CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.lignes
    ADD CONSTRAINT fk_cote FOREIGN KEY (cotation) REFERENCES bd.cote(cote);


--
-- Name: couennes fk_couenne; Type: FK CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.couennes
    ADD CONSTRAINT fk_couenne FOREIGN KEY (id_c) REFERENCES bd.lignes(id_l);


--
-- Name: croite fk_g; Type: FK CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.croite
    ADD CONSTRAINT fk_g FOREIGN KEY (id_g) REFERENCES bd.grimpeurs(id_g);


--
-- Name: croite fk_l; Type: FK CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.croite
    ADD CONSTRAINT fk_l FOREIGN KEY (id_l) REFERENCES bd.lignes(id_l);


--
-- Name: posts fk_m; Type: FK CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.posts
    ADD CONSTRAINT fk_m FOREIGN KEY (attachements) REFERENCES bd.media(id_m);


--
-- Name: lignes fk_secteur; Type: FK CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.lignes
    ADD CONSTRAINT fk_secteur FOREIGN KEY (secteur) REFERENCES bd.secteurs(id_s);


--
-- Name: circuits fk_secteur; Type: FK CONSTRAINT; Schema: bd; Owner: group_m1_db
--

ALTER TABLE ONLY bd.circuits
    ADD CONSTRAINT fk_secteur FOREIGN KEY (secteur) REFERENCES bd.secteurs(id_s);


--
-- PostgreSQL database dump complete
--


SELECT c.id,
       ln.last_name,
       fn.first_name,
       mn.middle_name,
       s.street_name,
       c.building_number,
       c.building_unit,
       c.apartment,
       c.phone
FROM contacts_contact c
         JOIN contacts_lastname ln ON c.last_name_id = ln.id
         JOIN contacts_firstname fn ON c.first_name_id = fn.id
         JOIN contacts_middlename mn ON c.middle_name_id = mn.id
         JOIN contacts_street s ON c.street_id = s.id;

SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM 
    Persons p
LEFT JOIN 
    Addresses a
ON
    p.personID = a.personID;

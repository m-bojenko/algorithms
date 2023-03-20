nodes = ['Regent’s Park', 'Goodge Street', 'Bayswater', 'Warren Street', 'Aldgate', 'Farringdon', 'Barbican', 'Russell Square', 'High Street Kensington', 'Old Street',
         'Green Park', 'Baker Street', 'Notting Hill Gate', 'Mansion House', 'Temple', 'Oxford Circus', 'Bond Street', 'Tower Hill', 'Westminster', 'Piccadilly Circus',
         'Charing Cross', 'Holborn', 'Tower Gateway', 'Monument', 'Moorgate', 'Leicester Square', 'St. Paul’s', 'Hyde Park Corner', 'Knightsbridge', 'Angel',
         'Queensway', 'Marble Arch', 'South Kensington', 'Sloane Square', 'Covent Garden', 'Liverpool Street', 'Great Portland Street', 'Bank', 'Chancery Lane',
         'Lancaster Gate', 'Holland Park', 'Cannon Street', 'Fenchurch Street', 'Gloucester Road', 'St. James’s Park', 'Euston Square' , 'Edgware Road', 'Embankment',
         'Blackfriars', 'Tottenham Court Road', 'King’s Cross St. Pancras', 'Paddington', 'Marylebone', 'Kensal Green', 'Queen’s Park', 'Bethnal Green',
         'Cambridge Heath', 'London Fields', 'Willesden Junction', 'Kilburn Park', 'Warwick Avenue', 'Maida Vale', 'Euston', 'Imperial Wharf', 'Clapham Junction',
         'Wapping', 'Denmark Hill', 'Whitechapel', 'Wandsworth Road', 'Rotherhithe', 'Shoreditch High Street', 'Haggerston', 'Hoxton', 'Shepherd’s Bush', 'Shadwell',
         'Canada Water', 'Fulham Broadway', 'West Brompton', 'Parsons Green', 'Putney Bridge', 'East Putney', 'Kensington (Olympia)', 'Aldgate East', 'Bethnal Green',
         'Mile End', 'Dalston Kingsland', 'Hackney Wick', 'Homerton', 'Hackney Central', 'Rectory Road', 'Hackney Downs', 'Dalston Junction', 'Canonbury',
         'Stepney Green', 'Highbury & Islington', 'Clapton', 'Stoke Newington', 'Upper Holloway', 'Gospel Oak', 'Island Gardens', 'Greenwich', 'Deptford Bridge',
         'South Quay', 'Crossharbour', 'Mudchute', 'Heron Quays', 'Elverson Road', 'Cutty Sark for Maritime Greenwich', 'Lewisham', 'Limehouse', 'Manor House',
         'Finsbury Park', 'Arsenal', 'Kentish Town West', 'Holloway Road', 'Caledonian Road', 'Hampstead', 'Belsize Park', 'Chalk Farm', 'Camden Town', 'Archway',
         'Tufnell Park', 'Kentish Town', 'Mornington Crescent', 'Camden Road', 'Caledonian Road & Barnsbury', 'Willesden Green', 'Swiss Cottage', 'Kilburn',
         'West Hampstead', 'Finchley Road', 'St. John’s Wood', 'Turnham Green', 'Stamford Brook', 'Ravenscourt Park' , 'West Kensington', 'Barons Court', 'Earl’s Court',
         'Shepherd’s Bush Market', 'Goldhawk Road', 'Hammersmith', 'Wood Lane', 'White City', 'Finchley Road & Frognal', 'Kensal Rise', 'Brondesbury Park', 'Brondesbury',
         'Kilburn High Road', 'South Hampstead', 'North Acton', 'East Acton', 'Southwark', 'Waterloo', 'London Bridge', 'Bermondsey', 'Vauxhall', 'Lambeth North',
         'Pimlico', 'Stockwell', 'Brixton', 'Elephant & Castle', 'Oval', 'Kennington', 'Borough']

init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["Reykjavik"]["Oslo"] = 5
init_graph["Reykjavik"]["London"] = 4
init_graph["Oslo"]["Berlin"] = 1
init_graph["Oslo"]["Moscow"] = 3
init_graph["Moscow"]["Belgrade"] = 5
init_graph["Moscow"]["Athens"] = 4
init_graph["Athens"]["Belgrade"] = 1
init_graph["Rome"]["Berlin"] = 2
init_graph["Rome"]["Athens"] = 2

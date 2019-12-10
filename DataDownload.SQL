SELECT gaiadr2.vari_rrlyrae.metallicity,  gaiadr2.gaia_source.parallax
FROM gaiadr2.vari_rrlyrae
JOIN gaiadr2.gaia_source
ON gaiadr2.vari_rrlyrae.source_id = gaiadr2.gaia_source.source_id
WHERE metallicity IS NOT NULL

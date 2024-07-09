select patient_id, patient_name, conditions
from patients
where conditions ~ '^DIAB1.*' or conditions ~ '.*\sDIAB1.*'
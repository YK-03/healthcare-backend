from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("patients", "0002_fix_created_by_fk"),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                ALTER TABLE patients_patient
                DROP CONSTRAINT IF EXISTS patients_patient_created_by_id_cf506306_fk_auth_user_id;

                ALTER TABLE patients_patient
                ADD CONSTRAINT patients_patient_created_by_id_accounts_user_id
                FOREIGN KEY (created_by_id)
                REFERENCES accounts_user (id)
                DEFERRABLE INITIALLY DEFERRED;
            """,
            reverse_sql="""
                ALTER TABLE patients_patient
                DROP CONSTRAINT IF EXISTS patients_patient_created_by_id_accounts_user_id;

                ALTER TABLE patients_patient
                ADD CONSTRAINT patients_patient_created_by_id_cf506306_fk_auth_user_id
                FOREIGN KEY (created_by_id)
                REFERENCES auth_user (id)
                DEFERRABLE INITIALLY DEFERRED;
            """,
        ),
    ]
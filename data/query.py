from dotenv import load_dotenv
import os
import psycopg

load_dotenv()

# Database connection
host = os.getenv("HOST")
database = os.getenv("DATABASE")
user = os.getenv("USER")
password = os.getenv("PASSWORD")

conn = psycopg.connect(host=host, dbname=database, user=user, password=password)


def getQuestName(id_quest:int):
    cur = conn.cursor()

    cur.execute(
        f"""
            SELECT "name"
            FROM "Quests"
            WHERE "id_quest" = {id_quest};
        """
    )

    quest_name = cur.fetchone()[0]

    cur.close()

    return quest_name


def getQuestDescription(id_quest:int):
    cur = conn.cursor()

    cur.execute(
        f"""
            SELECT "description"
            FROM "Quests"
            WHERE "id_quest" = {id_quest};
        """
    )

    quest_description = cur.fetchone()[0]

    cur.close()

    return quest_description


def getQuestExperienceReward(id_quest:int):
    cur = conn.cursor()

    cur.execute(
        f"""
            SELECT "experience_reward"
            FROM "Quests"
            WHERE "id_quest" = {id_quest};
        """
    )

    experience_reward = cur.fetchone()[0]

    cur.close()

    return experience_reward


def getQuestGoldReward(id_quest:int):
    cur = conn.cursor()

    cur.execute(
        f"""
            SELECT "gold_reward"
            FROM "Quests"
            WHERE "id_quest" = {id_quest};
        """
    )

    gold_reward = int(cur.fetchone()[0])

    cur.close()

    return gold_reward


def getTeacher(id_quest: int):
    cur = conn.cursor()

    cur.execute(
        f"""
            SELECT u.name, u.paternal_surname, u.maternal_surname
            FROM "Users" u
            JOIN "Teachers" t ON u.id_user = t.id_user
            JOIN "Teachers_Courses" tc ON t.id_teacher = tc.id_teacher
            JOIN "Teachers_Courses_Quests" tcq ON tc.id_teacher_course = tcq.id_teacher_course
            JOIN "Quests" q ON tcq.id_quest = q.id_quest
            WHERE q.id_quest = {id_quest};
        """
    )
    teacher = " ".join(cur.fetchone())
    
    cur.close()

    return teacher
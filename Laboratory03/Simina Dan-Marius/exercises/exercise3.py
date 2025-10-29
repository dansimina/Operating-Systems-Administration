#!/usr/bin/env python3

def main():
    with open("/etc/passwd", "r") as file:
        lines = file.readlines()

        print(f"Number of users is {len(lines)}")

        user = ""
        biggest_id = 0
        for line in lines:
            fields = line.split(":")
            id = int(fields[2])
            if biggest_id < id:
                biggest_id = id
                user = fields[0]
        
        print(f"The user with the biggest id is: {user}, with the id: {biggest_id}")

        able_to_login = list()
        for line in lines:
            fields = line.split(":")
            if fields[6].strip() not in ["/usr/sbin/nologin", "/bin/false"]:
                able_to_login.append(fields[0])
        print(f"The users which are able to login are:\n{able_to_login}")

if __name__ == "__main__":
    main()
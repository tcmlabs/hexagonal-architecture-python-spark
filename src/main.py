def count_lines(df):
    return df.count()


def say_hello(content):
    return f"Hello World! {content}"


if __name__ == "__main__":
    text = say_hello("Bob")
    print(text)

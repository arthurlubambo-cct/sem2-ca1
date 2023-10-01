import pandas as pd

f = open("list.txt", "r")
str = f.read()

lines = str.split("\n")


print(len(lines))
images = list(filter(lambda x: x.endswith('.jpg'),lines))

print(len(images))

df = pd.DataFrame({'path':images})
df['file_name'] = df['path'].apply(lambda x: x.split('/')[-1])
df['person_name'] = df['path'].apply(lambda x: x.split('/')[-2])
print(df)

gb_person = df.groupby("person_name").size().to_frame('size')
print(gb_person[gb_person['size']>1])
print(gb_person[gb_person['size']>1].mean())


import tomlkit

toml_data =""" [nested]  # Not necessary

     [nested.table]
     string       = "Hello, TOML!"
     weird_string = '''Literal
         Multiline'''
 """

print(tomlkit.dumps(tomlkit.loads(toml_data)))

print(tomlkit.dumps(tomlkit.loads(toml_data)) == toml_data)

# You can use loads() and dumps()—and load() and dump()—to read and write TOML as earlier. However, now all your string types, indentations, comments, and alignments are preserved

# create a TOML document from scratch
from tomlkit import comment, document, nl, table

toml = document()
toml.add(comment("writtern by TOML kit"))
toml.add(nl())
toml.add("board_size", 3)

# You convert toml to an actual TOML document by using dump() or dumps() as above, or you can use the .as_string() method

print(toml.as_string())

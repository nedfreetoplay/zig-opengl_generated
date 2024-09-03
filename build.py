import subprocess

gl_versions = {
    1: [0, 1, 2, 3, 4, 5],
    2: [0, 1],
    3: [0, 1, 2, 3],
    4: [0, 1, 2, 3, 4, 5, 6]
}

def build_gl(major, minor):
    gl_version = "GL_VERSION_%s_%s" % (major, minor)
    file_name = "gl%s%s.zig" % (major, minor)
    path_gl_xml = ".\\OpenGL-Registry\\xml\\gl.xml"
    command = "dotnet run %s %s %s" % (path_gl_xml, file_name, gl_version)
    proc = subprocess.Popen(command)
    proc.wait()

def main():
    for major in gl_versions.keys():
        for minor in gl_versions[major]:
            print("Generate OpenGL %s.%s" % (major, minor))
            build_gl(major, minor)

if __name__ == "__main__":
    main()
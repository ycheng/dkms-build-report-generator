
import apt.cache as ac

def process_dkms(dkms_list):
    c = ac.Cache()
    f = open(dkms_list, "r")
    # print(f)
    for pkg in f:
        pkg = pkg.strip("\n")
        lpkg = pkg + "-dkms"
        if lpkg in c:
            p = c[lpkg]
            # print("\t", p)
            print("apt-get", "-y", "install", lpkg)
            print("echo", "=============")
            print("dkms", "status", lpkg)
            print("echo", "=============")
            print("dkms", "status")
            print("echo", "=============")
            print("apt-get", "-y", "remove", lpkg)
            # for v in p.versions:
            #    print("\tver:", v.version)
            #    print("\tpriority:", v.policy_priority)
            pass
        else:
            print("\t", "# not found")
            pass


if False:
    p = c["apt"]
    print(p)
    print(p.architecture())
    print(p.candidate)
    print("Versions:")
    for v in p.versions:
        print("\t", v)
        print("\t", v.policy_priority)
        print("\t", v.raw_description)
        print("\t", v.uri)

def main():
    process_dkms("dkms.list")


if __name__ == "__main__":
    main()

fn main() {
    let vendor = buildsupport::vendor_dir();

    let mut lib = buildsupport::CxxLib::new("celcpp");
    lib.include(&vendor)
        .include_deps(&["absl", "protobuf", "re2", "antlr4rt"])
        .define("ANTLR4CPP_STATIC", None)
        .define("ANTLR4CPP_USING_ABSEIL", None)
        .files_from_filelist(&vendor);
    lib.compile();
    lib.export();
}
